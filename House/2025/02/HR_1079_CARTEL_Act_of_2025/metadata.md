# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1079?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1079
- Title: CARTEL Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1079
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2026-02-27T18:08:09Z
- Update date including text: 2026-02-27T18:08:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-06 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-06 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1079",
    "number": "1079",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "CARTEL Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-27T18:08:09Z",
    "updateDateIncludingText": "2026-02-27T18:08:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-06T18:15:40Z",
              "name": "Referred to"
            }
          },
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WI"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "GA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "FL"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NY"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "VA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MI"
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
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MS"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "UT"
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1079ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1079\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Mr. Luttrell (for himself, Mr. Steil , Mr. Webster of Florida , Mr. Collins , Mr. Gimenez , Mr. Garbarino , Mrs. Kiggans of Virginia , Mr. Bergman , Mr. McCaul , Mr. Babin , Mr. Crenshaw , Mr. Ezell , Mr. Weber of Texas , and Mr. Owens ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo publicize U.S. Customs and Border Protection operational statistics and report on foreign terrorist organizations.\n#### 1. Short title\nThis Act may be cited as the Cartel And Radical Terrorist Enforcement Log Act of 2025 or the CARTEL Act of 2025 .\n#### 2. Publication by U.S. Customs and Border Protection of Operational Statistics\nNot later than the seventh day of each month beginning with the second full month after the date of the enactment of this Act, the Commissioner of U.S. Customs and Border Protection shall publish on a publicly available website of the Department of Homeland Security information relating to the total number of alien encounters and nationalities, unique alien encounters and nationalities, gang affiliated apprehensions and nationalities, drug seizures, alien encounters included in the terrorist screening database and nationalities, arrests of criminal aliens or individuals wanted by law enforcement and nationalities, known got aways, encounters with deceased aliens, alien encounters and apprehensions affiliated with transnational criminal organizations, and all other related or associated statistics recorded by U.S. Customs and Border Protection during the immediately preceding month. Each such publication shall include the following:\n**(1)**\nThe total number of individuals included in the terrorist screening database (as such term is defined in section 2101 of the Homeland Security Act of 2002 ( 6 U.S.C. 621 )) who have repeatedly attempted to cross unlawfully into the United States.\n**(2)**\nThe total number of individuals included in the terrorist screening database who have been apprehended, including information relating to whether such individuals were released into the United States or removed.\n**(3)**\nThe total number of individuals affiliated with transnational criminal organizations who have repeatedly attempted to cross unlawfully into the United States.\n**(4)**\nThe total number of individuals affiliated with transnational criminal organizations who have been apprehended, including information relating to whether such individuals were released into the United States or removed.\n#### 3. Report to Congress on foreign terrorist organizations and transnational criminal organizations\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, and annually thereafter, the Secretary of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate an assessment of foreign terrorist organizations and transnational criminal organizations attempting to move their members or affiliates into the United States through the southern, northern, or maritime border.\n##### (b) Definition\nIn this section, the term foreign terrorist organization means an organization described in section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).",
      "versionDate": "2025-02-06",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-03-12T13:01:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119hr1079",
          "measure-number": "1079",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2026-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1079v00",
            "update-date": "2026-02-27"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Cartel And Radical Terrorist Enforcement Log Act of 2025 or the CARTEL Act of 2025</strong></p><p>This bill requires U.S. Customs and Border Protection to publish each month statistics related to encounters and arrests. The report must include, for example, the total number of individuals affiliated with transnational criminal organizations who have repeatedly attempted to cross unlawfully into the United States.</p><p>The Department of Homeland Security must report annually on foreign terrorist organizations and transnational criminal organizations attempting to move their members or affiliates into the United States through the southern, northern, or maritime border.</p>"
        },
        "title": "CARTEL Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1079.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cartel And Radical Terrorist Enforcement Log Act of 2025 or the CARTEL Act of 2025</strong></p><p>This bill requires U.S. Customs and Border Protection to publish each month statistics related to encounters and arrests. The report must include, for example, the total number of individuals affiliated with transnational criminal organizations who have repeatedly attempted to cross unlawfully into the United States.</p><p>The Department of Homeland Security must report annually on foreign terrorist organizations and transnational criminal organizations attempting to move their members or affiliates into the United States through the southern, northern, or maritime border.</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119hr1079"
    },
    "title": "CARTEL Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cartel And Radical Terrorist Enforcement Log Act of 2025 or the CARTEL Act of 2025</strong></p><p>This bill requires U.S. Customs and Border Protection to publish each month statistics related to encounters and arrests. The report must include, for example, the total number of individuals affiliated with transnational criminal organizations who have repeatedly attempted to cross unlawfully into the United States.</p><p>The Department of Homeland Security must report annually on foreign terrorist organizations and transnational criminal organizations attempting to move their members or affiliates into the United States through the southern, northern, or maritime border.</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119hr1079"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1079ih.xml"
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
      "title": "CARTEL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CARTEL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cartel And Radical Terrorist Enforcement Log Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To publicize U.S. Customs and Border Protection operational statistics and report on foreign terrorist organizations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T05:18:28Z"
    }
  ]
}
```
