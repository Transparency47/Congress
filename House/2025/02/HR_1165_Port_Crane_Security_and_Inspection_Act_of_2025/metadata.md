# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1165?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1165
- Title: Port Crane Security and Inspection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1165
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2025-04-08T13:48:14Z
- Update date including text: 2025-04-08T13:48:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-10 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-02-10 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1165",
    "number": "1165",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000593",
        "district": "28",
        "firstName": "Carlos",
        "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
        "lastName": "Gimenez",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Port Crane Security and Inspection Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-08T13:48:14Z",
    "updateDateIncludingText": "2025-04-08T13:48:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-10T18:16:34Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
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
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-10",
      "state": "VA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "LA"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TN"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1165ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1165\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Gimenez (for himself, Mr. Garamendi , Mrs. Kiggans of Virginia , Mrs. Luna , Mr. Donalds , Mr. Higgins of Louisiana , and Mr. Green of Tennessee ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo require the inspection of certain foreign cranes before use at a United States port, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Port Crane Security and Inspection Act of 2025 .\n#### 2. Foreign crane inspection transportation and port security and maritime security enhancement\n##### (a) In general\nWith respect to newly constructed foreign cranes procured for use at a United States port determined by the Secretary to be of high risk to port security or maritime transportation security and that connect to the internet, the Secretary of Homeland Security shall, acting through the Cybersecurity and Infrastructure Security Agency, before such crane is placed into service at such port, inspect such crane for potential security risks or threats.\n##### (b) Security risks or threats assessments\nNot later than 180 days after the date of enactment of this Act, the Secretary shall\u2014\n**(1)**\nassess the threat posed by security risks or threats of any existing or newly constructed foreign cranes in use at a United States port; and\n**(2)**\ntake any crane that poses a security risk or threat offline until such crane can be certified as no longer being a risk or threat.\n##### (c) Report to Congress\nNot later than 1 year after the date of enactment of this Act, the Secretary shall brief the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate regarding foreign crane security risks or threats posed by existing or newly constructed foreign cranes within United States ports.\n##### (d) Definitions\nIn this section:\n**(1) Covered foreign country**\nThe term covered foreign country means a country that\u2014\n**(A)**\nthe intelligence community has identified as a foreign adversary in its most recent Annual Threat Assessment; or\n**(B)**\nthe Secretary of Homeland Security, in coordination with the Director of National Intelligence, has identified as a foreign adversary that is not included in such Annual Threat Assessment.\n**(2) Foreign crane**\nThe term foreign crane means a crane for which any information technology and operational technology components in such crane that is connected into cyber infrastructure at a port located in the United States was, in whole or in part, manufactured by an entity that is operating under ownership, control, or influence of a covered foreign country.\n#### 3. Foreign crane prohibition\n##### (a) In general\nNotwithstanding any other provision of law, a foreign crane\u2014\n**(1)**\nfor which a contract was entered into on or after the date of enactment of this Act may not be operated at a port located in the United States; and\n**(2)**\noperated at a port located in the United States may not operate foreign software on any date after the date which is 5 years after the date of enactment of this Act.\n##### (b) Definitions\nIn this section:\n**(1) Covered foreign country**\nThe term covered foreign country means a country that\u2014\n**(A)**\nthe intelligence community has identified as a foreign adversary in its most recent Annual Threat Assessment; or\n**(B)**\nthe Secretary of Homeland Security, in coordination with the Director of National Intelligence, has identified as a foreign adversary that is not included in such Annual Threat Assessment.\n**(2) Foreign crane**\nThe term foreign crane means a crane for which any software or other technology in such crane that is connected into cyber infrastructure at a port located in the United States was, in whole or in part, manufactured by an entity that is owned or controlled by, is a subsidiary of, or is otherwise related legally or financially to a corporation based in a covered foreign country.\n**(3) Foreign software**\nThe term foreign software means software or other technology, in whole or in part, manufactured by a company wholly owned by a covered foreign country.",
      "versionDate": "2025-02-10",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-14T11:52:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119hr1165",
          "measure-number": "1165",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1165v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Port Crane Security and Inspection Act of 2025 </strong></p><p>This bill limits the operation of foreign cranes at U.S. ports. In general,<em>\u00a0foreign cranes </em>are those that\u00a0have information technology and operational technology components that (1) were manufactured by companies that are subject to the ownership, control, or influence of a country designated as a foreign adversary; and (2) connect to ports' cyber infrastructure.</p><p>Foreign cranes that are contracted for on or after the date of the bill's enactment may not operate at a U.S. port. Also, beginning five years after this bill is enacted, foreign cranes operating at U.S. ports may not use software or other technology manufactured by a company owned by a country designated as a foreign adversary.</p><p>Additionally, the Cybersecurity and Infrastructure Security Agency (CISA) must (1) inspect foreign cranes\u00a0for potential security risks or threats before they are placed into operation, (2) assess the threat posed by security risks or threats of existing or newly constructed foreign cranes, and (3) take any crane that poses a security risk or threat offline until the crane can be certified as no longer being a risk or threat.</p><p>CISA must also report to Congress about security risks or threats posed by foreign cranes at U.S. ports.</p>"
        },
        "title": "Port Crane Security and Inspection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1165.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Port Crane Security and Inspection Act of 2025 </strong></p><p>This bill limits the operation of foreign cranes at U.S. ports. In general,<em>\u00a0foreign cranes </em>are those that\u00a0have information technology and operational technology components that (1) were manufactured by companies that are subject to the ownership, control, or influence of a country designated as a foreign adversary; and (2) connect to ports' cyber infrastructure.</p><p>Foreign cranes that are contracted for on or after the date of the bill's enactment may not operate at a U.S. port. Also, beginning five years after this bill is enacted, foreign cranes operating at U.S. ports may not use software or other technology manufactured by a company owned by a country designated as a foreign adversary.</p><p>Additionally, the Cybersecurity and Infrastructure Security Agency (CISA) must (1) inspect foreign cranes\u00a0for potential security risks or threats before they are placed into operation, (2) assess the threat posed by security risks or threats of existing or newly constructed foreign cranes, and (3) take any crane that poses a security risk or threat offline until the crane can be certified as no longer being a risk or threat.</p><p>CISA must also report to Congress about security risks or threats posed by foreign cranes at U.S. ports.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr1165"
    },
    "title": "Port Crane Security and Inspection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Port Crane Security and Inspection Act of 2025 </strong></p><p>This bill limits the operation of foreign cranes at U.S. ports. In general,<em>\u00a0foreign cranes </em>are those that\u00a0have information technology and operational technology components that (1) were manufactured by companies that are subject to the ownership, control, or influence of a country designated as a foreign adversary; and (2) connect to ports' cyber infrastructure.</p><p>Foreign cranes that are contracted for on or after the date of the bill's enactment may not operate at a U.S. port. Also, beginning five years after this bill is enacted, foreign cranes operating at U.S. ports may not use software or other technology manufactured by a company owned by a country designated as a foreign adversary.</p><p>Additionally, the Cybersecurity and Infrastructure Security Agency (CISA) must (1) inspect foreign cranes\u00a0for potential security risks or threats before they are placed into operation, (2) assess the threat posed by security risks or threats of existing or newly constructed foreign cranes, and (3) take any crane that poses a security risk or threat offline until the crane can be certified as no longer being a risk or threat.</p><p>CISA must also report to Congress about security risks or threats posed by foreign cranes at U.S. ports.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr1165"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1165ih.xml"
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
      "title": "Port Crane Security and Inspection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Port Crane Security and Inspection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the inspection of certain foreign cranes before use at a United States port, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:18:26Z"
    }
  ]
}
```
