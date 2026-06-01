# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/858?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/858
- Title: REVIVE VI Act
- Congress: 119
- Bill type: HR
- Bill number: 858
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-06-06T13:22:28Z
- Update date including text: 2025-06-06T13:22:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/858",
    "number": "858",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "E000298",
        "district": "4",
        "firstName": "Ron",
        "fullName": "Rep. Estes, Ron [R-KS-4]",
        "lastName": "Estes",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "REVIVE VI Act",
    "type": "HR",
    "updateDate": "2025-06-06T13:22:28Z",
    "updateDateIncludingText": "2025-06-06T13:22:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:08:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "VI"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OK"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "AL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "WV"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "OH"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr858ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 858\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Estes (for himself, Ms. Plaskett , Mr. Hern of Oklahoma , Ms. Sewell , Mr. Feenstra , and Mr. Schneider ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to determine global intangible low-taxed income without regard to certain income derived from services performed in the Virgin Islands.\n#### 1. Short title\nThis Act may be cited as the Restore Economic Vitality and Investment in the Virgin Islands Act or the REVIVE VI Act .\n#### 2. Global intangible low-taxed income determined without regard to certain income derived from services performed in the Virgin Islands\n##### (a) In general\nSection 951A(c)(2)(A)(i) of the Internal Revenue Code of 1986 is amended by striking and at the end of subclause (IV), by striking the period at the end of subclause (V) and inserting , and , and by adding at the end the following new subclause:\n(VI) in the case of any specified United States shareholder, any qualified Virgin Islands services income. .\n##### (b) Definitions and special rules\nSection 951A(c)(2) of such Code is amended by adding at the end the following new subparagraph:\n(C) Provisions related to qualified Virgin Islands services income For purposes of subparagraph (A)(i)(VI)\u2014 (i) Qualified Virgin Islands services income The term qualified Virgin Islands services income means any gross income which satisfies all of the following requirements: (I) Such gross income is compensation for labor or personal services (within the meaning of section 862(a)(3)) performed in the Virgin Islands by a corporation formed under the laws of the Virgin Islands. (II) Such gross income is attributable to services performed from within the Virgin Islands by individuals for the benefit of such corporation. (III) Such gross income is effectively connected with the conduct of a trade or business within the Virgin Islands. (ii) Specified United States shareholder The term specified United States shareholder means any United States shareholder which is\u2014 (I) an individual, trust, or estate, or (II) a closely held C corporation (as defined in section 469(j)(1)) if such corporation acquired its direct or indirect equity interest in the foreign corporation which derived the qualified Virgin Islands services income before December 31, 2023. (iii) Regulations The Secretary shall prescribe such regulations or other guidance as may be necessary or appropriate to carry out this subparagraph and subparagraph (A)(i)(VI), including regulations or other guidance to prevent the abuse of such subparagraphs. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years of foreign corporations beginning after the date of the enactment of this Act, and to taxable years of United States shareholders with or within which such taxable years of foreign corporations end.",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-05-22",
        "actionTime": "06:56:39",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Big Beautiful Bill Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1605",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "International Competition for American Jobs Act",
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
        "name": "Taxation",
        "updateDate": "2025-04-04T20:55:56Z"
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
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr858ih.xml"
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
      "title": "REVIVE VI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REVIVE VI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restore Economic Vitality and Investment in the Virgin Islands Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to determine global intangible low-taxed income without regard to certain income derived from services performed in the Virgin Islands.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T08:18:35Z"
    }
  ]
}
```
