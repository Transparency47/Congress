# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2571?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2571
- Title: Self-Insurance Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2571
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-05-28T17:50:26Z
- Update date including text: 2026-05-28T17:50:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-06-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 21 - 15.
- 2025-12-15 - Calendars: Placed on the Union Calendar, Calendar No. 356.
- 2025-12-15 - Committee: Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-408.
- 2025-12-15 - Committee: Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-408.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-06-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 21 - 15.
- 2025-12-15 - Calendars: Placed on the Union Calendar, Calendar No. 356.
- 2025-12-15 - Committee: Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-408.
- 2025-12-15 - Committee: Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-408.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2571",
    "number": "2571",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "O000177",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Onder, Robert [R-MO-3]",
        "lastName": "Onder",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Self-Insurance Protection Act",
    "type": "HR",
    "updateDate": "2026-05-28T17:50:26Z",
    "updateDateIncludingText": "2026-05-28T17:50:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-12-15",
      "calendarNumber": {
        "calendar": "U00356"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 356.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-12-15",
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
      "text": "Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-408.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-408.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 21 - 15.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
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
      "actionDate": "2025-04-01",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
            "date": "2025-12-15T18:09:41Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-25T13:12:58Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-01T14:06:00Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "IN"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2571ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2571\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Onder introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to exclude from the definition of health insurance coverage certain medical stop-loss insurance obtained by certain plan sponsors of group health plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Self-Insurance Protection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSmall and large employers offer health benefit plan coverage to employees in self-funded arrangements using company assets or a fund, or by paying premiums to purchase fully-insured coverage from a health insurance company.\n**(2)**\nEmployers that self-fund health benefit plans will often purchase stop-loss insurance as a financial risk management tool to protect against excess or unexpected catastrophic health plan claims losses that arise above projected costs paid out of company assets.\n**(3)**\nStop-loss coverage insures the employer sponsoring the health benefit plan against unforeseen health plan claims, does not insure the employee health benefit plan itself, and does not pay health care providers for medical services provided to the employees.\n**(4)**\nEmployer-sponsored health benefit plans are regulated under the Employee Retirement Income Security Act of 1974, however, States regulate the availability and the coverage terms of stop-loss insurance coverage that employers purchase to protect company assets and to protect a fund against excess or unexpected claims losses.\n**(5)**\nBoth large and small employers that choose to self-fund must also be able to protect company assets or a fund against excess or unexpected claims losses and States must reasonably regulate stop-loss insurance to assure its availability to both large and small employers.\n#### 3. Certain medical stop-loss insurance obtained by certain plan sponsors of group health plans not included under the definition of health insurance coverage\nSection 733(b)(1) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1191b(b)(1) ) is amended by adding at the end the following sentence: Such term shall not include a stop-loss policy obtained by a self-insured group health plan or a plan sponsor of a group health plan that self-insures the health risks of its plan participants to reimburse the plan or sponsor for losses that the plan or sponsor incurs in providing health or medical benefits to such plan participants in excess of a predetermined level set forth in the stop-loss policy obtained by such plan or sponsor. .\n#### 4. Effect on other laws\nSection 514(b) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1144(b) ) is amended by adding at the end the following:\n(10) The provisions of this title (including part 7 relating to group health plans) shall preempt State laws insofar as they may now or hereafter prevent an employee benefit plan that is a group health plan from insuring against the risk of excess or unexpected health plan claims losses. .",
      "versionDate": "2025-04-01",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2571rh.xml",
      "text": "IB\nUnion Calendar No. 356\n119th CONGRESS\n1st Session\nH. R. 2571\n[Report No. 119\u2013408]\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Onder introduced the following bill; which was referred to the Committee on Education and Workforce\nDecember 15, 2025 Additional sponsors: Mr. Messmer and Mr. Grothman\nDecember 15, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on April 1, 2025\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to exclude from the definition of health insurance coverage certain medical stop-loss insurance obtained by certain plan sponsors of group health plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Self-Insurance Protection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSmall and large employers offer health benefit plan coverage to employees in self-funded arrangements using company assets or a fund, or by paying premiums to purchase fully-insured coverage from a health insurance company.\n**(2)**\nEmployers that self-fund health benefit plans will often purchase stop-loss insurance as a financial risk management tool to protect against excess or unexpected catastrophic health plan claims losses that arise above projected costs paid out of company assets.\n**(3)**\nStop-loss coverage insures the employer sponsoring the health benefit plan against unforeseen health plan claims, does not insure the employee health benefit plan itself, and does not pay health care providers for medical services provided to the employees.\n**(4)**\nEmployer-sponsored health benefit plans are regulated under the Employee Retirement Income Security Act of 1974.\n**(5)**\nHowever, States regulate the availability and the coverage terms of stop-loss insurance coverage that employers purchase to protect company assets and to protect a fund from excess or unexpected claims losses.\n**(6)**\nBoth large and small employers that choose to self-fund must also be able to protect company assets or a fund against excess or unexpected claims losses and States must reasonably regulate stop-loss insurance to assure its availability to both large and small employers.\n#### 3. Certain medical stop-loss insurance obtained by certain plan sponsors of group health plans not included under the definition of health insurance coverage\nSection 733(b)(1) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1191b(b)(1) ) is amended by adding at the end the following sentence: Such term shall not include a stop-loss policy obtained by a self-insured group health plan or a plan sponsor of a group health plan that self-insures the health risks of its plan participants to reimburse the plan or sponsor for losses that the plan or sponsor incurs in providing health or medical benefits to such plan participants in excess of a predetermined level set forth in the stop-loss policy obtained by such plan or sponsor. .\n#### 4. Effect on other laws\nSection 514(b) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1144(b) ) is amended by adding at the end the following:\n(10) The provisions of this title (including part 7 relating to group health plans) shall preempt State laws insofar as they may now or hereafter prevent an employee benefit plan that is a group health plan from insuring against the risk of excess or unexpected health plan claims losses. .",
      "versionDate": "2025-12-15",
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
            "name": "Employee benefits and pensions",
            "updateDate": "2025-06-27T17:22:45Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-27T17:22:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-04-06T14:19:59Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2571ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2571rh.xml"
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
      "title": "Self-Insurance Protection Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-12-16T06:38:15Z"
    },
    {
      "title": "Self-Insurance Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Self-Insurance Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Employee Retirement Income Security Act of 1974 to exclude from the definition of health insurance coverage certain medical stop-loss insurance obtained by certain plan sponsors of group health plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:30Z"
    }
  ]
}
```
