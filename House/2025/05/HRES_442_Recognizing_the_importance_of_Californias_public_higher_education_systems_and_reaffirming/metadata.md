# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/442?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/442
- Title: Recognizing the importance of California's public higher education systems and reaffirming the United States' commitment to supporting these institutions.
- Congress: 119
- Bill type: HRES
- Bill number: 442
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-12-10T09:05:35Z
- Update date including text: 2025-12-10T09:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-05-23 - IntroReferral: Submitted in House
- 2025-05-23 - IntroReferral: Submitted in House
- Latest action: 2025-05-23: Submitted in House

## Actions

- 2025-05-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-05-23 - IntroReferral: Submitted in House
- 2025-05-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/442",
    "number": "442",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001287",
        "district": "6",
        "firstName": "Ami",
        "fullName": "Rep. Bera, Ami [D-CA-6]",
        "lastName": "Bera",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Recognizing the importance of California's public higher education systems and reaffirming the United States' commitment to supporting these institutions.",
    "type": "HRES",
    "updateDate": "2025-12-10T09:05:35Z",
    "updateDateIncludingText": "2025-12-10T09:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-23T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres442ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 442\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Bera (for himself, Mr. Obernolte , Mr. Carbajal , Mr. Garamendi , Mr. Takano , Ms. Simon , Mr. Panetta , Ms. Barrag\u00e1n , Mr. Harder of California , Ms. Friedman , Ms. S\u00e1nchez , Mr. DeSaulnier , Mr. Mullin , Mr. Min , Mr. Tran , Mr. Lieu , Mrs. Torres of California , Ms. Matsui , and Mr. Gomez ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nRecognizing the importance of California\u2019s public higher education systems and reaffirming the United States commitment to supporting these institutions.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the importance of California\u2019s public higher education systems in driving the economy of California and contributing to the status of the United States as a world-leading economy;\n**(2)**\nacknowledges the substantial work done by California\u2019s Public Higher Education Systems in providing students from traditionally underserved and low-income communities opportunities for educational attainment, economic growth, and personal and professional development at their institutions;\n**(3)**\ncommends the inventions and achievements of students from California\u2019s public colleges in advancing technological, educational, and social progress; and\n**(4)**\nreaffirms unwavering commitment to supporting California\u2019s public higher education systems\u2014the University of California, the California State University, and the California Community Colleges.",
      "versionDate": "2025-05-23",
      "versionType": "IH"
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
        "name": "Education",
        "updateDate": "2025-06-26T10:27:53Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres442ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing the importance of California's public higher education systems and reaffirming the United States' commitment to supporting these institutions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T06:18:41Z"
    },
    {
      "title": "Recognizing the importance of California's public higher education systems and reaffirming the United States' commitment to supporting these institutions.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-24T08:05:35Z"
    }
  ]
}
```
