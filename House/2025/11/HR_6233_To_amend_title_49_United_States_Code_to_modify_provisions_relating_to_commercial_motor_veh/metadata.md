# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6233?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6233
- Title: Commercial Motor Vehicle English Proficiency Act
- Congress: 119
- Bill type: HR
- Bill number: 6233
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-03-05T09:06:31Z
- Update date including text: 2026-03-05T09:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-21 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-21 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6233",
    "number": "6233",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David J. [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Commercial Motor Vehicle English Proficiency Act",
    "type": "HR",
    "updateDate": "2026-03-05T09:06:31Z",
    "updateDateIncludingText": "2026-03-05T09:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-21T18:26:51Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WY"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "GA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KS"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WI"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "WI"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "IN"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "KS"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "SC"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "AK"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6233ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6233\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Taylor (for himself, Ms. Hageman , Mr. Steube , Mr. Carter of Georgia , Mr. Mann , Mr. Van Orden , Mrs. Miller of Illinois , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to modify provisions relating to commercial motor vehicle operator testing requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Commercial Motor Vehicle English Proficiency Act .\n#### 2. Commercial motor vehicle operator testing requirements\n##### (a) Testing standards\nSection 31305(a) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (4), by redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and indenting the clauses appropriately;\n**(2)**\nin paragraph (5)\u2014\n**(A)**\nin subparagraph (B), by redesignating clauses (i) through (iv) as subclauses (I) through (IV), respectively, and indenting the subclauses appropriately; and\n**(B)**\nby redesignating subparagraphs (A) through (C) as clauses (i) through (iii), respectively, and indenting the clauses appropriately;\n**(3)**\nin paragraph (8), by redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and indenting the clauses appropriately;\n**(4)**\nby redesignating paragraphs (1) through (8) as subparagraphs (A) through (H), respectively, and indenting the subparagraphs appropriately;\n**(5)**\nin the matter preceding subparagraph (A) (as so redesignated)\u2014\n**(A)**\nin the second sentence, by striking The regulations and inserting the following:\n(2) Requirements The regulations under paragraph (1) ; and\n**(B)**\nin the first sentence, by striking The Secretary of Transportation shall prescribe regulations on and inserting the following:\n(1) In general The Secretary of Transportation (referred to in this section as the Secretary ) shall prescribe regulations establishing ; and\n**(6)**\nby adding at the end the following:\n(3) English language proficiency (A) In general Notwithstanding any other provision of law (including regulations), effective beginning on the date that is 2 years after the date of enactment of the Commercial Motor Vehicle English Proficiency Act , an individual shall not be eligible to pass a knowledge test, in written, verbal, or automated format, under this subsection, or to receive a certification of fitness to operate a commercial motor vehicle, unless the individual demonstrates the ability to understand in English the basic information needed to effectively operate, and to communicate in English while operating, a commercial motor vehicle, including\u2014 (i) reading and understanding traffic signs in English; (ii) communicating in English with traffic safety officers, border patrol agents, agricultural checkpoint officers, and cargo weight-limit station personnel; and (iii) providing and receiving feedback and directions in English. (B) Prohibition Notwithstanding any other provision of law (including regulations), effective beginning on the date that is 2 years after the date of enactment of the Commercial Motor Vehicle English Proficiency Act , a knowledge test, in written, verbal, or automated format, under this subsection may not be administered in any language other than English. .\n##### (b) Amendment to regulations\nThe Secretary of Transportation shall modify the regulations contained in part 383 of title 49, Code of Federal Regulations, as the Secretary of Transportation determines to be necessary to implement this section and the amendments made by this section by the date that is 2 years after the date of enactment of this Act.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2114",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Commercial Motor Vehicle English Proficiency Act",
      "type": "S"
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
        "updateDate": "2025-12-18T16:52:34Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6233ih.xml"
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
      "title": "Commercial Motor Vehicle English Proficiency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T07:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commercial Motor Vehicle English Proficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T07:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to modify provisions relating to commercial motor vehicle operator testing requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T07:33:38Z"
    }
  ]
}
```
