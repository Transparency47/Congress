# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1554?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1554
- Title: Freedom from Government Competition Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1554
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-04-14T08:05:35Z
- Update date including text: 2026-04-14T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1554",
    "number": "1554",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Freedom from Government Competition Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:35Z",
    "updateDateIncludingText": "2026-04-14T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "VA"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "IN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AL"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "FL"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1554ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1554\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Bean of Florida (for himself, Mr. Cline , and Mr. Stutzman ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require that the Federal Government procure from the private sector the goods and services necessary for the operations and management of certain Government agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom from Government Competition Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nPrivate sector business concerns, which are free to respond to the private or public demands of the marketplace, constitute the strength of the United States economic system.\n**(2)**\nCompetitive private enterprises are the most productive, efficient, and effective sources of goods and services.\n**(3)**\nUnfair Government competition with the private sector of the economy is detrimental to the United States economic system.\n**(4)**\nUnfair Government competition with the private sector of the economy is at an unacceptably high level, both in scope and in dollar volume.\n**(5)**\nCurrent law and policy have failed to address adequately the problem of unfair Government competition with the private sector of the economy.\n**(6)**\nIt is in the public interest that the Federal Government establish a consistent policy to rely on the private sector of the economy to provide goods and services necessary for or beneficial to the operation and management of Federal agencies and to avoid unfair Government competition with the private sector of the economy.\n#### 3. Definitions\nIn this Act, the term agency means\u2014\n**(1)**\nan executive department as defined by section 101 of title 5, United States Code;\n**(2)**\na military department as defined by section 102 of such title; and\n**(3)**\nan independent establishment as defined by section 104(l) of such title.\n#### 4. Procurement from private sources\n##### (a) Policy\nIn the process of governing, the Federal Government should not compete with its citizens. The competitive enterprise system, characterized by individual freedom and initiative, is the primary source of national economic strength. In recognition of this principle, it has been and continues to be the general policy of the Federal Government\u2014\n**(1)**\nto rely on commercial sources to supply the products and services the Government needs;\n**(2)**\nto refrain from providing a product or service if the product or service can be procured more economically from a commercial source; and\n**(3)**\nto utilize Federal employees to perform inherently governmental functions (as that term is defined in section 5 of the Federal Activities Inventory Reform Act of 1998 ( Public Law 105\u2013270 ; 112 Stat. 2384)).\n##### (b) General rule\nExcept as provided in subsection (c) and notwithstanding any other provision of law, each agency shall obtain all goods and services necessary for or beneficial to the accomplishment of its authorized functions by procurement from private sources.\n##### (c) Exemptions\nSubsection (b) shall not apply to an agency with respect to goods or services if\u2014\n**(1)**\nthe goods or services are required by law to be produced or performed, respectively, by the agency; or\n**(2)**\nthe head of the agency determines and certifies to Congress in accordance with regulations promulgated by the Director of the Office of Management and Budget that\u2014\n**(A)**\nFederal Government production, manufacture, or provision of a good or service is necessary for the national defense or homeland security;\n**(B)**\na good or service is so critical to the mission of the agency or so inherently governmental in nature that it is in the public interest to require production or performance, respectively, by Government employees; or\n**(C)**\nthere is no private source capable of providing the good or service.\n##### (d) Method of procurement\nThe provision of goods and services not exempt by subsection (c)(1) or (c)(2) shall be performed by an entity in the private sector through\u2014\n**(1)**\nthe divestiture of Federal involvement in the provision of a good or service;\n**(2)**\nthe award of a contract to an entity in the private sector, using competitive procedures, as defined in section 152 of title 41, United States Code, and section 2302 of title 10, United States Code; or\n**(3)**\nconducting a public-private competitive sourcing analysis in accordance with the procedures established by the Office of Management and Budget and determining that using the assets, facilities, and performance of the private sector is in the best interest of the United States and that production or performance, respectively, by the private sector provides the best value to the taxpayer.\n##### (e) Contracted activities\nThe head of an agency may utilize Federal employees to provide goods or services previously provided by an entity in the private sector upon completion of a public-private competitive sourcing analysis described in subsection (d)(3), and after making a determination that the provision of such goods or services by Federal employees provides the best value to the taxpayer.\n##### (f) Regulations\nThe Director of the Office of Management and Budget shall promulgate such regulations as the Director considers necessary to carry out this section. In promulgating such regulations, the Director shall assure that any State or territory, or political subdivision of a State or territory, complies with the policy and implements the requirements of this section when expending Federal funds.\n#### 5. Study and report\nThe Director of the Office of Management and Budget, after consultation with the Comptroller General of the United States, shall carry out a study to evaluate the activities carried out in each agency, including those identified as commercial and inherently governmental in nature in the inventory prepared pursuant to the Federal Activities Inventory Reform Act of 1998 ( Public Law 105\u2013270 ; 31 U.S.C. 501 note) and shall transmit a report to the Congress prior to June 30 of each year. The report shall include\u2014\n**(1)**\nan evaluation of the justification for exempting activities pursuant to section 4(c); and\n**(2)**\na schedule for the transfer of commercial activities to the private sector, pursuant to section 4(d), to be completed within 5 years after the date on which such report is transmitted to the Congress.",
      "versionDate": "2025-02-25",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T20:34:43Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-17T20:34:28Z"
          },
          {
            "name": "Office of Management and Budget (OMB)",
            "updateDate": "2025-07-17T20:34:33Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-07-17T20:34:03Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-07-17T20:34:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-08T13:42:36Z"
      }
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1554ih.xml"
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
      "title": "Freedom from Government Competition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom from Government Competition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require that the Federal Government procure from the private sector the goods and services necessary for the operations and management of certain Government agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:19:10Z"
    }
  ]
}
```
