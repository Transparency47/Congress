# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7541?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7541
- Title: U.S. Farmworker Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 7541
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-02-25T17:42:18Z
- Update date including text: 2026-02-25T17:42:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7541",
    "number": "7541",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "J000298",
        "district": "7",
        "firstName": "Pramila",
        "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
        "lastName": "Jayapal",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "U.S. Farmworker Protection Act",
    "type": "HR",
    "updateDate": "2026-02-25T17:42:18Z",
    "updateDateIncludingText": "2026-02-25T17:42:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:04:20Z",
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
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
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
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7541ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7541\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Ms. Jayapal (for herself, Ms. Pelosi , Mr. Garc\u00eda of Illinois , Mr. Castro of Texas , Mr. Casar , Ms. Chu , Ms. Simon , Mr. Thanedar , and Mr. Doggett ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo protect United States workers by creating annual restrictions on the H\u20132A temporary worker program.\n#### 1. Short title\nThis Act may be cited as the U.S. Farmworker Protection Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe H\u20132A program, as created by section 218 of the Immigration and Nationality Act ( 8 U.S.C. 1188 ), has experienced unprecedented growth in recent years;\n**(2)**\nwith the H\u20132A program having 384,865 certified jobs in fiscal year 2024, an increase of 40 percent compared to fiscal year 2020 (when there were 275,430 certified jobs), an increase of 71 percent compared to fiscal year 2017 (when there were 224,965 certified jobs), and an almost 5-time increase compared to fiscal year 2008 (when there were 82,099 certified jobs); and\n**(3)**\nthe unlimited growth of the H\u20132A program threatens to displace United States farmworkers and depress the wages and working conditions of United States farmworkers, including those who harvest crops, drive trucks, and operate equipment.\n#### 3. Creating annual restrictions on the H\u20132A program\n##### (a) Annual restriction established\nSection 218(a) of the Immigration and Nationality Act ( 8 U.S.C. 1188(a) ) is amended by adding at the end the following:\n(3) The Secretary of Labor may not certify petitions covering more than 400,000 positions for a fiscal year. For purposes of this paragraph, any position that the petitioner, in the petition, specifies will be filled by a worker who is represented by a bargaining representative shall not be counted towards the limit under this paragraph. .\n##### (b) Definition of bargaining representative\nSection 218(i) of the Immigration and Nationality Act ( 8 U.S.C. 1188(i) ) is amended by adding at the end the following:\n(3) The term bargaining representative means a labor organization (as such term is defined in section 2 of the National Labor Relations Act ( 29 U.S.C. 152 )) that\u2014 (A) represents agricultural employees in their employment relations with agricultural employers; and (B) has filed an LM\u20132, LM\u20133, or LM\u20134 form (or any successor form) with the Secretary of Labor and has a collective bargaining agreement covering agricultural employees. .",
      "versionDate": "2026-02-12",
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
        "updateDate": "2026-02-25T17:42:18Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7541ih.xml"
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
      "title": "U.S. Farmworker Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "U.S. Farmworker Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect United States workers by creating annual restrictions on the H-2A temporary worker program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:03:26Z"
    }
  ]
}
```
