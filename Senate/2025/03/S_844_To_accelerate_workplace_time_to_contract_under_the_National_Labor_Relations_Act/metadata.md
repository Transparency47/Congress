# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/844?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/844
- Title: Faster Labor Contracts Act
- Congress: 119
- Bill type: S
- Bill number: 844
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/844",
    "number": "844",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Faster Labor Contracts Act",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-04",
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
        "item": [
          {
            "date": "2025-03-04T22:22:59Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-04T22:22:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NJ"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "OH"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "AZ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "AZ"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "VA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "DE"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NH"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "CO"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s844is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 844\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Hawley (for himself, Mr. Booker , Mr. Peters , Mr. Moreno , and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo accelerate workplace time-to-contract under the National Labor Relations Act.\n#### 1. Short title\nThis Act may be cited as the Faster Labor Contracts Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEmployees in the United States have a right to organize collectively in order to secure higher wages and other benefits, and regularly exercise that right by voting to be represented by a labor organization in their workplaces.\n**(2)**\nA successful vote in favor of representation by a labor organization does not immediately lead to an agreement between the parties. Often the negotiation process is difficult and protracted, taking a year or longer.\n**(3)**\nResearch indicates that these contracting delays are increasing over time. A Bloomberg Law study from 2021 found that the average number of days between a vote in favor of representation by a labor organization and a contract entered into between the parties was 465 days.\n**(4)**\nDelays in the processing of collective bargaining contracts primarily benefit employers opposed to representation by the labor organization. The employers can use those delays to sap labor organization resolve and secure more favorable terms for the employer.\n**(5)**\nIn order for employees in the United States to fully enjoy the benefits guaranteed to them by Federal labor law, those employees must be able to promptly secure a first contract following the legal recognition or certification of a labor organization, and Federal labor law ought to facilitate this expediency.\n#### 3. Facilitating initial collective bargaining agreements\nSection 8 of the National Labor Relations Act ( 29 U.S.C. 158 ) is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nby redesignating paragraphs (1) through (4) as subparagraphs (A) through (D), respectively;\n**(B)**\nby striking For the purposes of this section and inserting (1) For the purposes of this section ;\n**(C)**\nby inserting (and to maintain current wages, hours, and terms and conditions of employment pending an agreement) after arising thereunder ;\n**(D)**\nby inserting : Provided , That an employer\u2019s duty to collectively bargain shall continue absent decertification of the representative following an election conducted pursuant to section 9 after making of a concession ;\n**(E)**\nby inserting further before , That where there is in effect ;\n**(F)**\nby striking The duties imposed and inserting (2) The duties imposed ;\n**(G)**\nby striking by paragraphs (2), (3), and (4) and inserting by subparagraphs (B), (C), and (D) of paragraph (1) ;\n**(H)**\nby striking section 8(d)(1) and inserting paragraph (1)(A) ;\n**(I)**\nby striking section 8(d)(3) each place it appears and inserting paragraph (1)(C) ;\n**(J)**\nby striking section 8(d)(4) and inserting paragraph (1)(D) ; and\n**(K)**\nby adding at the end the following:\n(3) Whenever collective bargaining is for the purpose of establishing an initial collective bargaining agreement following certification or recognition of an individual or labor organization as a representative as provided under section 9(a), the following shall apply: (A) Not later than 10 days after receiving a written request for collective bargaining from an individual or labor organization that has been newly recognized or certified as a representative as provided under section 9(a), or within such further period as the parties agree upon, the parties shall meet and begin bargaining collectively, and shall make every reasonable effort to conclude and sign a collective bargaining agreement. (B) If after the expiration of the 90-day period beginning on the date on which bargaining is commenced, or such additional period as the parties may agree upon, the parties have failed to reach an agreement, either party may notify the Federal Mediation and Conciliation Service that a dispute exists, and may request mediation. Whenever such a request is received, the Service shall promptly communicate with the parties and use its best efforts, by mediation and conciliation, to secure an agreement. (C) If after the expiration of the 30-day period beginning on the date on which the request for mediation is made under subparagraph (B), or such additional period as the parties may agree upon, the Service is not able to bring the parties to agreement by conciliation, the Service shall refer the dispute to a 3-person arbitration panel established in accordance with such regulations as may be prescribed by the Service, with one member selected by the individual or labor organization, one member selected by the employer, and one neutral member mutually agreed to by the parties. The individual or labor organization and the employer must each select the members of the 3-person arbitration panel within 14 days of the Service\u2019s referral; if the individual or labor organization or the employer fail to do so, the Service shall designate any members not selected by the individual or labor organization or by the employer. A majority of the 3-person arbitration panel shall render a decision settling the dispute and such decision shall be binding upon the parties for a period of 2 years, unless amended during such period by written consent of the parties. Such decision shall be based on\u2014 (i) the employer\u2019s financial status and prospects; (ii) the size and type of the employer\u2019s operations and business; (iii) the employees\u2019 cost of living; (iv) the employees\u2019 ability to sustain themselves, their families, and their dependents on the wages and benefits they earn from the employer; and (v) the wages and benefits other employers in the same business provide their employees. ; and\n**(2)**\nin subsection (g), by striking clause (B) of the last sentence of section 8(d) of this Act and inserting subsection (d)(2)(B) .\n#### 4. GAO report examining average workplace time-to-contract\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report examining the average number of days between\u2014\n**(1)**\nthe date on which an individual or labor organization is certified or recognized as the representative of employees under section 9(a) of the National Labor Relations Act ( 29 U.S.C. 159(a) ), following the date of enactment of this Act; and\n**(2)**\nthe date on which the parties enter into an initial collective bargaining agreement.",
      "versionDate": "2025-03-04",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-16",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "5408",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Faster Labor Contracts Act",
      "type": "HR"
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
            "name": "Alternative dispute resolution, mediation, arbitration",
            "updateDate": "2026-02-17T20:09:50Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-17T20:09:45Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-17T20:10:02Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2026-02-17T20:09:39Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-02-17T20:09:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-28T11:33:31Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s844is.xml"
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
      "title": "Faster Labor Contracts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to accelerate workplace time-to-contract under the National Labor Relations Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:33:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Faster Labor Contracts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:23:20Z"
    }
  ]
}
```
