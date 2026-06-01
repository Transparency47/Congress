# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1260?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1260
- Title: U.S. Park Police Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 1260
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-05-20T08:08:26Z
- Update date including text: 2026-05-20T08:08:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1260",
    "number": "1260",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "U.S. Park Police Modernization Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:26Z",
    "updateDateIncludingText": "2026-05-20T08:08:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:01:45Z",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NV"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MT"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "MS"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "NE"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NJ"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NY"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "AZ"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "MN"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1260ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1260\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo reduce the number of, and shorten the time between, pay grade steps for officers and members of the United States Park Police, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the U.S. Park Police Modernization Act .\n#### 2. Condensing the service steps for united states park police officers and members\n##### (a) In general\nSection 501(c)(1) of the District of Columbia Police and Firemen\u2019s Salary Act of 1958 (sec. 5\u2013545.01(c)(1), D.C. Official Code) is amended to read as follows:\n(1) The annual rates of basic compensation of officers and members of the United States Park Police, serving in classes corresponding or similar to those in the salary schedule in \u00a7 5\u2013541.01 shall be fixed in accordance with the following schedule of rates: Salary class and title Step 1 Step 2 Step 3 Step 4 Step 5 Step 6 Step 7 1 The rate of basic pay for positions in Salary Class 5, 7, 8, and 9 is limited to 95 percent of the rate of pay for level V of the Executive Schedule. 2 The rate of basic pay for positions in Salary Class 10 will be equal to 95 percent of the rate of pay for level V of the Executive Schedule. 3 The rate of basic pay for positions in Salary Class 11 will be equal to the rate of pay for level V of the Executive Schedule. Time between steps 52 weeks 104 weeks Years in service 0 1 2 3 5 7 9 1: Private 55,801 59,084 61,808 66,141 70,531 73,244 75,989 1: Private (Technician) 59,149 62,629 65,516 70,109 74,763 77,639 80,548 1: Private (Pilot) 59,707 63,220 66,135 70,771 75,468 78,371 81,308 3: Detective 68,353 71,774 75,205 78,626 82,003 85,436 4: Sergeant (Line) 74,449 78,147 81,851 85,587 89,322 4: Sergeant (Detective) 78,916 82,836 86,762 90,722 94,681 4: Sergeant (Technician) 78,916 82,836 86,762 90,722 94,681 4: Sergeant (Pilot) 79,660 83,617 87,581 91,578 95,575 5: Lieutenant 1 82,119 86,225 91,205 95,356 7: Captain 1 96,453 101,294 106,126 8: Inspector/Major 1 9: Deputy Chief 1 10: Assistant Chief 2 11: Chief, United States Park Police 3 Salary class and title Step 8 Step 9 Step 10 Step 11 Step 12 Step 13 1 The rate of basic pay for positions in Salary Class 5, 7, 8, and 9 is limited to 95 percent of the rate of pay for level V of the Executive Schedule. 2 The rate of basic pay for positions in Salary Class 10 will be equal to 95 percent of the rate of pay for level V of the Executive Schedule. 3 The rate of basic pay for positions in Salary Class 11 will be equal to the rate of pay for level V of the Executive Schedule. Time between steps 104 weeks Years in service 11 13 15 17 19 22 1: Private 78,720 81,448 86,197 89,353 91,995 94,739 1: Private (Technician) 83,443 86,335 91,369 94,714 97,515 100,423 1: Private (Pilot) 84,230 87,149 92,231 95,608 98,435 101,371 3: Detective 88,854 92,264 98,732 102,149 105,585 108,745 4: Sergeant (Line) 93,054 96,773 102,522 106,227 109,964 113,245 4: Sergeant (Detective) 98,637 102,579 108,673 112,601 116,562 120,040 4: Sergeant (Technician) 98,637 102,579 108,673 112,601 116,562 120,040 4: Sergeant (Pilot) 99,568 103,547 109,699 113,663 117,661 121,172 5: Lieutenant 1 99,489 103,628 109,990 114,105 118,211 121,738 7: Captain 1 110,887 115,715 123,038 127,898 132,772 136,756 8: Inspector/Major 1 129,860 135,428 141,344 148,089 153,959 159,770 9: Deputy Chief 1 154,791 161,215 167,645 173,945 173,945 173,945 10: Assistant Chief 2 173,945 11: Chief, United States Park Police 3 183,100 .\n##### (b) Service step adjustments\nSection 303(a)(5) of the District of Columbia Police and Fireman\u2019s Salary Act of 1958 (sec. 5\u2013543.03(a)(5), D.C. Official Code) is amended\u2014\n**(1)**\nin subparagraph (B), by striking or 9 and inserting 9, 10, or 11 ;\n**(2)**\nin subparagraph (C), by striking 10 and inserting 12 ; and\n**(3)**\nby striking subparagraph (D).\n##### (c) Prior adjustments disregarded\nAny adjustments to the annual rates of basic compensation of officers or members of the United States Park Police under section 501(c)(2) of the District of Columbia Police and Firemen\u2019s Salary Act of 1958 (sec. 5\u2013545.01(c)(2), D.C. Official Code) on or before January 12, 2025, shall be disregarded.\n##### (d) Rule of construction\nThis section may not be construed as limiting or reducing any payment under section 501(c)(3) of the District of Columbia Police and Firemen\u2019s Salary Act of 1958 (sec. 5\u2013545.01(c)(3), D.C. Official Code).\n##### (e) Effective date\nThis section and the amendments made by this section shall take effect on the first day of the first pay period beginning on or after the date of the enactment of this Act.",
      "versionDate": "2025-02-12",
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
            "name": "Department of the Interior",
            "updateDate": "2025-07-03T13:53:14Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-03T13:53:21Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-07-03T13:53:30Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-07-03T13:57:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-07T17:58:15Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1260ih.xml"
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
      "title": "U.S. Park Police Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "U.S. Park Police Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reduce the number of, and shorten the time between, pay grade steps for officers and members of the United States Park Police, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T09:18:26Z"
    }
  ]
}
```
