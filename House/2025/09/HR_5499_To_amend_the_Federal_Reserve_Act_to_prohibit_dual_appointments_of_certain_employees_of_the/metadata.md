# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5499?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5499
- Title: Fed Integrity and Independence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5499
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-02-26T09:07:05Z
- Update date including text: 2026-02-26T09:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5499",
    "number": "5499",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "V000130",
        "district": "52",
        "firstName": "Juan",
        "fullName": "Rep. Vargas, Juan [D-CA-52]",
        "lastName": "Vargas",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Fed Integrity and Independence Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-26T09:07:05Z",
    "updateDateIncludingText": "2026-02-26T09:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:05:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "OH"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "LA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5499ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5499\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Vargas introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Federal Reserve Act to prohibit dual appointments of certain employees of the Federal Reserve System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fed Integrity and Independence Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe independence of the Federal Reserve System from political interference from the President is fundamental to the effective operation of the central bank.\n**(2)**\nCongress structured the Federal Reserve System to ensure that its monetary policy decisions focus on achieving long-run goals and do not become subject to political pressures from the President that could lead to undesirable outcomes.\n**(3)**\nTo protect this independence, Congress made it so members of the Board of Governors of the Federal Reserve System are appointed for staggered 14-year terms, and the Chairman of the Board of Governors is appointed for a four-year term.\n##### (b) Sense of Congress\nIt is the sense of Congress that it is not appropriate for any employee appointed by the President\u2014whether they are on leave or not\u2014to serve as a member of the Board of Governors of the Federal Reserve System.\n#### 3. Prohibition of Dual Appointment\n##### (a) Board of Governors\nThe fourth sentence of the first undesignated paragraph of section 10 of the Federal Reserve Act ( 12 U.S.C. 241 ) is amended by striking business of the Board and shall each receive and inserting business of the Board, may not simultaneously hold any other office, position, or employment for which the member is appointed by the President, including under a leave of absence from such other office, position, or employment, and shall each receive .\n##### (b) Federal Reserve Bank Presidents; First Vice President of the Federal Reserve Bank of New York\nThe fifth subparagraph of the fourth undesignated paragraph of section 4 of the Federal Reserve Act ( 12 U.S.C. 341 ) is amended\u2014\n**(1)**\nby inserting after the second sentence (relating to presidents of Federal reserve banks) the following: A president of the bank may not simultaneously hold any other office, position, or employment for which the president is appointed by the President, including under a leave of absence from such other office, position, or employment. ; and\n**(2)**\nby inserting after the third sentence (relating to first vice presidents of Federal reserve banks) the following: The first vice president of the Federal Reserve Bank of New York may not simultaneously hold any other office, position, or employment for which the first vice president is appointed by the President, including under a leave of absence from such other office, position, or employment. .\n##### (c) Rule of application\nAn individual serving as a governor of the Board of Governors of the Federal Reserve System, the president of a Federal reserve bank, or the first vice president of the Federal Reserve Bank of New York on the date of enactment of this Act and who is ineligible to serve in such position due to the amendments made by this section are hereby terminated from such position on the date of enactment of this Act.",
      "versionDate": "2025-09-18",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-16T15:22:03Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5499ih.xml"
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
      "title": "Fed Integrity and Independence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fed Integrity and Independence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T08:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Reserve Act to prohibit dual appointments of certain employees of the Federal Reserve System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T08:48:38Z"
    }
  ]
}
```
