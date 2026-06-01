# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/32?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/32
- Title: No Bailout for Sanctuary Cities Act
- Congress: 119
- Bill type: HR
- Bill number: 32
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-08-16T08:05:24Z
- Update date including text: 2025-08-16T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/32",
    "number": "32",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "No Bailout for Sanctuary Cities Act",
    "type": "HR",
    "updateDate": "2025-08-16T08:05:24Z",
    "updateDateIncludingText": "2025-08-16T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IA"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IN"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "OK"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "NC"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "AL"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "AL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "PA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "KY"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "GA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr32ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 32\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. LaLota (for himself, Mr. Feenstra , Mrs. Houchin , Mr. McCaul , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide that sanctuary jurisdictions that provide benefits to aliens who are present in the United States without lawful status under the immigration laws are ineligible for Federal funds intended to benefit such aliens.\n#### 1. Short title\nThis Act may be cited as the No Bailout for Sanctuary Cities Act .\n#### 2. Sanctuary jurisdiction defined\n##### (a) In general\nExcept as provided under subsection (b), for purposes of this Act, the term sanctuary jurisdiction means any State or political subdivision of a State that has in effect a statute, ordinance, policy, or practice that prohibits or restricts any government entity or official from\u2014\n**(1)**\nsending, receiving, maintaining, or exchanging with any Federal, State, or local government entity information regarding the citizenship or immigration status (lawful or unlawful) of any individual; or\n**(2)**\ncomplying with a request lawfully made by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act (8 U.S.C. 1226 and 1357) to comply with a detainer for, or notify about the release of, an individual.\n##### (b) Exception\nA State or political subdivision of a State shall not be deemed a sanctuary jurisdiction based solely on its having a policy whereby its officials will not share information regarding, or comply with a request made by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act (8 U.S.C. 1226 and 1357) to comply with a detainer regarding, an individual who comes forward as a victim or a witness to a criminal offense.\n#### 3. Sanctuary jurisdictions ineligible for certain Federal funds\nBeginning on the earlier of the date that is 60 days after the date of enactment of this Act or the first day of the fiscal year that begins after the date of enactment of this Act, a sanctuary jurisdiction is ineligible to receive any Federal funds that the sanctuary jurisdiction intends to use for the benefit (including the provision of food, shelter, healthcare services, legal services, and transportation) of aliens who are present in the United States without lawful status under the immigration laws (as such terms are defined in section 101 of the Immigration and Nationality Act).\n#### 4. Report on noncompliance\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary of Homeland Security shall submit to the Committee on the Judiciary of the House of Representatives and the Committee on the Judiciary of the Senate a report that includes a list of States, and political subdivisions of States, that have failed to comply with requests described in section 2(a)(2).",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-06-03T18:16:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-03T18:16:48Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-06-03T18:16:48Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-06-03T18:16:48Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-06-03T18:16:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-03T14:59:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr32",
          "measure-number": "32",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr32v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Bailout for Sanctuary Cities Act</strong></p><p>This bill makes a state or political subdivision of a state ineligible for any federal funds that the jurisdiction intends to use to benefit non-U.S. nationals (i.e., <em>aliens </em>under federal law) who are unlawfully present if the jurisdiction withholds information about citizenship or immigration status or does not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;\u00a0</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or\u00a0</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply\u00a0to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>DHS must annually provide to specified congressional committees a list of jurisdictions that have failed to comply with a DHS detainer or have failed to notify DHS of an individual\u2019s release.</p><p>The funding restriction begins 60 days after the bill's enactment or on the first day of\u00a0the fiscal year following\u00a0the bill's enactment, whichever is earlier.</p>"
        },
        "title": "No Bailout for Sanctuary Cities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr32.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Bailout for Sanctuary Cities Act</strong></p><p>This bill makes a state or political subdivision of a state ineligible for any federal funds that the jurisdiction intends to use to benefit non-U.S. nationals (i.e., <em>aliens </em>under federal law) who are unlawfully present if the jurisdiction withholds information about citizenship or immigration status or does not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;\u00a0</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or\u00a0</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply\u00a0to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>DHS must annually provide to specified congressional committees a list of jurisdictions that have failed to comply with a DHS detainer or have failed to notify DHS of an individual\u2019s release.</p><p>The funding restriction begins 60 days after the bill's enactment or on the first day of\u00a0the fiscal year following\u00a0the bill's enactment, whichever is earlier.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hr32"
    },
    "title": "No Bailout for Sanctuary Cities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Bailout for Sanctuary Cities Act</strong></p><p>This bill makes a state or political subdivision of a state ineligible for any federal funds that the jurisdiction intends to use to benefit non-U.S. nationals (i.e., <em>aliens </em>under federal law) who are unlawfully present if the jurisdiction withholds information about citizenship or immigration status or does not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;\u00a0</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or\u00a0</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply\u00a0to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>DHS must annually provide to specified congressional committees a list of jurisdictions that have failed to comply with a DHS detainer or have failed to notify DHS of an individual\u2019s release.</p><p>The funding restriction begins 60 days after the bill's enactment or on the first day of\u00a0the fiscal year following\u00a0the bill's enactment, whichever is earlier.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hr32"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr32ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "No Bailout for Sanctuary Cities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Bailout for Sanctuary Cities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that sanctuary jurisdictions that provide benefits to aliens who are present in the United States without lawful status under the immigration laws are ineligible for Federal funds intended to benefit such aliens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T10:48:21Z"
    }
  ]
}
```
