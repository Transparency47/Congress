# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6551?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6551
- Title: New BANK Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6551
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 455.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-530.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-530.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 455.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-530.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-530.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6551",
    "number": "6551",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000583",
        "district": "11",
        "firstName": "Barry",
        "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
        "lastName": "Loudermilk",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "New BANK Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-25",
      "calendarNumber": {
        "calendar": "U00455"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 455.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-25",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-530.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-530.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
        "item": [
          {
            "date": "2026-02-25T18:50:56Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T20:12:32Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T20:12:23Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:01:25Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6551ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6551\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Loudermilk introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require annual reports on national bank and Federal savings association charter applications, depository institution holding company applications, Federal deposit insurance applications, and State depository institution charter applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the New Bank Application Numbers Knowledge Act of 2025 or the New BANK Act of 2025 .\n#### 2. Annual report on national bank and Federal savings association charter applications\nThe Comptroller of the Currency shall publish an annual report that includes\u2014\n**(1)**\nthe number of national bank and Federal savings association charter applications received, approved on a preliminary basis, approved on a final basis, denied, withdrawn, expired, mooted, or returned;\n**(2)**\nthe mean and median times for preliminary approval of such applications;\n**(3)**\nthe mean and median times for final approval of such applications; and\n**(4)**\ncommon reasons leading to denial, withdrawal, or expiration of preliminary approval of such applications.\n#### 3. Annual report on Federal credit union charter applications\nThe National Credit Union Administration Board shall publish an annual report that includes\u2014\n**(1)**\nthe number of Federal credit union charter applications received, proofs of concept established, approved on a final basis, denied, withdrawn, expired, mooted, or returned;\n**(2)**\nthe mean and median times to establish proof of concept for such applications;\n**(3)**\nthe mean and median times for final approval of such applications; and\n**(4)**\ncommon reasons leading to denial, withdrawal, or expiration of establishment of proof of concept of such applications.\n#### 4. Annual report on depository institution holding company applications\nThe Board of Governors of the Federal Reserve System shall publish an annual report that includes\u2014\n**(1)**\nthe number of applications to become a top-tier depository institution holding company received, approved, denied, withdrawn, mooted, or returned;\n**(2)**\nthe mean and median times to approve such applications; and\n**(3)**\ncommon reasons leading to denial or withdrawal of such applications.\n#### 5. Annual report on Federal deposit insurance applications\nThe Federal Deposit Insurance Corporation shall publish an annual report that includes\u2014\n**(1)**\nthe number of applications for deposit insurance received, approved, denied, withdrawn, mooted, or returned;\n**(2)**\nthe mean and median times to approve such applications; and\n**(3)**\ncommon reasons leading to denial or withdrawal of such applications.\n#### 6. Annual report on State depository institution and State credit union charter applications\n##### (a) In general\nThe Board of Governors of the Federal Reserve System, the Federal Deposit Insurance Corporation, and the National Credit Union Administration Board shall, jointly, and in consultation with State banking regulators and State credit union regulators, publish an annual report that includes\u2014\n**(1)**\nthe number of State depository institution charter applications received, approved, denied, withdrawn, or otherwise dispositioned by State banking regulators and State credit union regulators, with numbers for each State shown separately;\n**(2)**\nthe mean and median times to approve such applications, with times for each State shown separately; and\n**(3)**\ncommon reasons leading to denial or withdrawal of such applications.\n##### (b) Definitions\nIn this section:\n**(1) State**\nThe term State means any State of the United States, the District of Columbia, and any territory of the United States.\n**(2) State bank**\nThe term State bank means any bank, banking association, trust company, savings bank, industrial bank, or other banking institution incorporated under the laws of any State.\n**(3) State depository institution**\nThe term State depository institution means\u2014\n**(A)**\na State bank or a State savings association; and\n**(B)**\na State credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) State savings association**\nThe term State savings association means\u2014\n**(A)**\nany building and loan association, savings and loan association, or homestead association incorporated under the laws of any State; and\n**(B)**\nany cooperative bank incorporated under the laws of any State that is not a State bank.",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6551rh.xml",
      "text": "IB\nUnion Calendar No. 455\n119th CONGRESS\n2d Session\nH. R. 6551\n[Report No. 119\u2013530]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Loudermilk introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsors: Mr. Gottheimer and Mr. Lawler\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo require annual reports on national bank and Federal savings association charter applications, depository institution holding company applications, Federal deposit insurance applications, and State depository institution charter applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the New Bank Application Numbers Knowledge Act of 2025 or the New BANK Act of 2025 .\n#### 2. Annual report on national bank and Federal savings association charter applications\nThe Comptroller of the Currency shall publish an annual report that includes the following, or with respect to any equivalent procedure used by the Office of Comptroller of the Currency includes the following:\n**(1)**\nThe number of national bank and Federal savings association charter applications received, approved on a preliminary basis, approved on a final basis, denied, withdrawn, expired, mooted, or returned.\n**(2)**\nThe mean and median times for preliminary approval of such applications.\n**(3)**\nThe mean and median times for final approval of such applications.\n**(4)**\nTo the extent practicable, common reasons leading to the denial, withdrawal, or expiration of preliminary approval of such applications.\n#### 3. Annual report on Federal credit union charter applications\nThe National Credit Union Administration shall publish an annual report that includes the following, or with respect to any equivalent procedure used by the Administration includes the following:\n**(1)**\nThe number of Federal credit union charter applications received, approved on a final basis, denied, withdrawn, inactive, or returned pending resubmission.\n**(2)**\nThe mean and median times for final approval of such applications.\n**(3)**\nTo the extent practicable, common reasons leading to application denial, withdrawal, inactivity, or to applications being returned for resubmission.\n#### 4. Annual report on depository institution holding company applications\nThe Board of Governors of the Federal Reserve System shall publish an annual report that includes the following, or with respect to any equivalent procedure used by the Board of Governors includes the following:\n**(1)**\nThe number of applications to become a top-tier depository institution holding company received, approved, denied, withdrawn, mooted, or returned.\n**(2)**\nThe mean and median times to approve such applications.\n**(3)**\nTo the extent practicable, common reasons leading to denial or withdrawal of such applications.\n#### 5. Annual report on Federal deposit insurance applications\nThe Federal Deposit Insurance Corporation shall publish an annual report that includes the following, or with respect to any equivalent procedure used by the Corporation includes the following:\n**(1)**\nThe number of applications for deposit insurance received, approved, denied, withdrawn, mooted, or returned.\n**(2)**\nThe mean and median times to approve such applications.\n**(3)**\nTo the extent practicable, common reasons leading to denial or withdrawal of such applications.\n#### 6. Annual report on State depository institution and State credit union charter applications\n##### (a) In general\nThe Board of Governors of the Federal Reserve System, the Federal Deposit Insurance Corporation, and the National Credit Union Administration Board shall, jointly, and in consultation with State banking regulators and State credit union regulators, publish an annual report that includes the following, or with respect to any equivalent procedure used by such agencies includes the following:\n**(1)**\nThe number of State depository institution charter applications received, approved, denied, withdrawn, or otherwise dispositioned by State banking regulators and State credit union regulators, with numbers for each State shown separately.\n**(2)**\nThe mean and median times to approve such applications, with times for each State shown separately.\n**(3)**\nTo the extent practicable, common reasons leading to denial or withdrawal of such applications.\n##### (b) Definitions\nIn this section:\n**(1) State**\nThe term State means any State of the United States, the District of Columbia, and any territory of the United States.\n**(2) State bank**\nThe term State bank means any bank, banking association, trust company, savings bank, industrial bank, or other banking institution incorporated under the laws of any State.\n**(3) State depository institution**\nThe term State depository institution means\u2014\n**(A)**\na State bank or a State savings association; and\n**(B)**\na State credit union, as defined in section 101 of the Federal Credit Union Act ( 12 U.S.C. 1752 ).\n**(4) State savings association**\nThe term State savings association means\u2014\n**(A)**\nany building and loan association, savings and loan association, or homestead association incorporated under the laws of any State; and\n**(B)**\nany cooperative bank incorporated under the laws of any State that is not a State bank.",
      "versionDate": "2026-02-25",
      "versionType": "Reported in House"
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-01-06T17:07:58Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-06T17:06:19Z"
          },
          {
            "name": "Financial crises and stabilization",
            "updateDate": "2026-01-06T17:04:32Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-06T17:05:37Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-01-06T17:06:25Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-01-06T17:04:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T18:46:04Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6551ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6551rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "New BANK Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:38:14Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "New Bank Application Numbers Knowledge Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:38:14Z"
    },
    {
      "title": "New BANK Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "New BANK Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "New Bank Application Numbers Knowledge Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require annual reports on national bank and Federal savings association charter applications, depository institution holding company applications, Federal deposit insurance applications, and State depository institution charter applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T09:03:22Z"
    }
  ]
}
```
