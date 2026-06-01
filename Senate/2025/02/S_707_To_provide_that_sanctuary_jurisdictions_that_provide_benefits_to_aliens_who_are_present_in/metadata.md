# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/707?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/707
- Title: No Bailout for Sanctuary Cities Act
- Congress: 119
- Bill type: S
- Bill number: 707
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2026-01-06T22:38:44Z
- Update date including text: 2026-01-06T22:38:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/707",
    "number": "707",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "No Bailout for Sanctuary Cities Act",
    "type": "S",
    "updateDate": "2026-01-06T22:38:44Z",
    "updateDateIncludingText": "2026-01-06T22:38:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-25T16:43:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "ID"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MO"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "UT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NE"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "IN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s707is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 707\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Risch (for himself, Mr. Crapo , Mr. Schmitt , Mr. Daines , Mr. Lee , Mr. Sheehy , Mr. Ricketts , Mr. Banks , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide that sanctuary jurisdictions that provide benefits to aliens who are present in the United States without lawful status under the immigration laws are ineligible for Federal funds intended to benefit such aliens.\n#### 1. Short title\nThis Act may be cited as the No Bailout for Sanctuary Cities Act .\n#### 2. Definition of sanctuary jurisdiction\n##### (a) In general\nExcept as provided in subsection (b), in this Act, the term sanctuary jurisdiction means any State or political subdivision of a State that has in effect a statute, ordinance, policy, or practice that prohibits or restricts any government entity or official from\u2014\n**(1)**\nsending, receiving, maintaining, or exchanging with any Federal, State, or local government entity information regarding the citizenship or immigration status (lawful or unlawful) of any individual; or\n**(2)**\ncomplying with a request lawfully made by the Secretary of Homeland Security under section 236 or 287 of the Immigration and Nationality Act ( 8 U.S.C. 1226 , 1357) to comply with a detainer for, or notify about the release of, an individual.\n##### (b) Exception\nFor purposes of this Act, a State or political subdivision of a State shall not be considered a sanctuary jurisdiction based solely on the State or political subdivision of a State having a policy under which officials of the State or political subdivision of a State will not share information with respect to, or comply with a request made by the Secretary of Homeland Security under section 236 or 287 of the Immigration and Nationality Act ( 8 U.S.C. 1226 , 1357) to comply with a detainer for, an individual who comes forward as a victim of or a witness to a criminal offense.\n#### 3. Sanctuary jurisdictions ineligible for certain Federal funds\nBeginning on the date that is the earlier of the date that is 60 days after the date of the enactment of this Act or the first day of the fiscal year that begins after the date of the enactment of this Act, a sanctuary jurisdiction is ineligible to receive any Federal funds that the sanctuary jurisdiction intends to use for the benefit (including the provision of food, shelter, healthcare services, legal services, and transportation) of aliens who are present in the United States without lawful status under the immigration laws (as defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )).\n#### 4. Report on noncompliance\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the Secretary of Homeland Security shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that identifies each State and political subdivision of a State that has, within the preceding 1-year period, failed to comply with a request described in section 2(a)(2).",
      "versionDate": "2025-02-25",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-03-21T16:54:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
    "originChamber": "Senate",
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
          "measure-id": "id119s707",
          "measure-number": "707",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2026-01-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s707v00",
            "update-date": "2026-01-06"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>No Bailout for Sanctuary Cities Act</strong></p><p>This bill makes a state or political subdivision of a state ineligible for any federal funds that the jurisdiction intends to use to benefit non-U.S. nationals (i.e., <em>aliens </em>under federal law) who are unlawfully present if the jurisdiction withholds information about citizenship or immigration status or does not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;\u00a0</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or\u00a0</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply\u00a0to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>DHS must annually provide to specified congressional committees a list of jurisdictions that have failed to comply with a DHS detainer or have failed to notify DHS of an individual\u2019s release.</p><p>The funding restriction begins 60 days after the bill's enactment or on the first day of\u00a0the fiscal year following\u00a0the bill's enactment, whichever is earlier.</p>"
        },
        "title": "No Bailout for Sanctuary Cities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s707.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Bailout for Sanctuary Cities Act</strong></p><p>This bill makes a state or political subdivision of a state ineligible for any federal funds that the jurisdiction intends to use to benefit non-U.S. nationals (i.e., <em>aliens </em>under federal law) who are unlawfully present if the jurisdiction withholds information about citizenship or immigration status or does not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;\u00a0</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or\u00a0</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply\u00a0to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>DHS must annually provide to specified congressional committees a list of jurisdictions that have failed to comply with a DHS detainer or have failed to notify DHS of an individual\u2019s release.</p><p>The funding restriction begins 60 days after the bill's enactment or on the first day of\u00a0the fiscal year following\u00a0the bill's enactment, whichever is earlier.</p>",
      "updateDate": "2026-01-06",
      "versionCode": "id119s707"
    },
    "title": "No Bailout for Sanctuary Cities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Bailout for Sanctuary Cities Act</strong></p><p>This bill makes a state or political subdivision of a state ineligible for any federal funds that the jurisdiction intends to use to benefit non-U.S. nationals (i.e., <em>aliens </em>under federal law) who are unlawfully present if the jurisdiction withholds information about citizenship or immigration status or does not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;\u00a0</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or\u00a0</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply\u00a0to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>DHS must annually provide to specified congressional committees a list of jurisdictions that have failed to comply with a DHS detainer or have failed to notify DHS of an individual\u2019s release.</p><p>The funding restriction begins 60 days after the bill's enactment or on the first day of\u00a0the fiscal year following\u00a0the bill's enactment, whichever is earlier.</p>",
      "updateDate": "2026-01-06",
      "versionCode": "id119s707"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s707is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-03-21T04:08:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Bailout for Sanctuary Cities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide that sanctuary jurisdictions that provide benefits to aliens who are present in the United States without lawful status under the immigration laws are ineligible for Federal funds intended to benefit such aliens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:23Z"
    }
  ]
}
```
