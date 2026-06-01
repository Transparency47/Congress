# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3812?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3812
- Title: STRIVE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3812
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2026-02-04T05:06:21Z
- Update date including text: 2026-02-04T05:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- 2025-11-07 - Calendars: Placed on the Union Calendar, Calendar No. 323.
- 2025-11-07 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-371.
- 2025-11-07 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-371.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-07-23 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-23 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- 2025-11-07 - Calendars: Placed on the Union Calendar, Calendar No. 323.
- 2025-11-07 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-371.
- 2025-11-07 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-371.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3812",
    "number": "3812",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000605",
        "district": "13",
        "firstName": "Adam",
        "fullName": "Rep. Gray, Adam [D-CA-13]",
        "lastName": "Gray",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "STRIVE Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:21Z",
    "updateDateIncludingText": "2026-02-04T05:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-11-07",
      "calendarNumber": {
        "calendar": "U00323"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 323.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-371.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-371.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
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
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
            "date": "2025-11-07T19:10:30Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-23T14:08:53Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-06T13:00:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "CA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "TX"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "TN"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "IL"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "MN"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "WA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3812ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3812\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Gray introduced the following bill; which was referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to prohibit the collection of a health care copayment by the Secretary of Veterans Affairs from a veteran under certain conditions attributable to a failure of the Department of Veterans Affairs to process certain information within applicable timeliness standards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Troubling Retroactive Invoices for Veteran Expenses Act of 2025 or the STRIVE Act of 2025 .\n#### 2. Prohibition on collection of health care copayments by the Secretary of Veterans Affairs under certain conditions; authority of the Secretary to waive health care copayments\nSection 1730A of title 38, United States Code, is amended\u2014\n**(1)**\nby striking the heading and inserting Prohibitions on collection of copayments under certain conditions ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin the heading, by striking Prohibition and inserting Prohibitions ; and\n**(B)**\nby striking the Secretary may not require and all that follows through the end of the subsection and inserting the following:\nthe Secretary may not require\u2014 (1) a covered veteran to make any copayment for the receipt of hospital care or medical services under the laws administered by the Secretary; (2) any veteran to make any copayment for the receipt of such hospital care or medical services after the end of the two-year period beginning on the date such veteran received such hospital care or medical services if the failure of the veteran to make such copayment during such period is attributable to the failure of an employee, official, or information system of the Department to process information provided by or on behalf of the veteran within applicable timeliness standards established by the Secretary; or (3) any veteran to make a copayment in an amount that exceeds $2,000 for the receipt of such hospital care or medical services if the amount of such copayment is attributable to an error on the part of an employee, official, or information system of the Department. ;\n**(3)**\nby redesignating subsection (b) as subsection (c); and\n**(4)**\nby inserting after subsection (a) the following new subsection:\n(b) Waiver authority The Secretary may waive the requirement for a veteran to make any copayment for the receipt of such hospital care or medical services in any case in which the Secretary determines such a waiver would be appropriate, without regard to whether the veteran submits to the Secretary a request for such waiver. .",
      "versionDate": "2025-06-06",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3812rh.xml",
      "text": "IB\nUnion Calendar No. 323\n119th CONGRESS\n1st Session\nH. R. 3812\n[Report No. 119\u2013371]\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Gray introduced the following bill; which was referred to the Committee on Veterans' Affairs\nNovember 7, 2025 Additional sponsors: Mr. Takano , Mr. Castro of Texas , Mr. Cohen , Mrs. Ramirez , Ms. Ross , Ms. Craig , Ms. Jayapal , and Mr. Figures\nNovember 7, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on June 6, 2025\nA BILL\nTo amend title 38, United States Code, to prohibit the collection of a health care copayment by the Secretary of Veterans Affairs from a veteran under certain conditions attributable to a failure of the Department of Veterans Affairs to process certain information within applicable timeliness standards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Troubling Retroactive Invoices for Veteran Expenses Act of 2025 or the STRIVE Act of 2025 .\n#### 2. Prohibition on collection of health care copayments by the Secretary of Veterans Affairs under certain conditions; authority of the Secretary to waive health care copayments\n##### (a) In general\nSubchapter III of chapter 17 of title 38, United States Code, is amended by inserting after section 1722C the following new section:\n1722D. Copayments: prohibitions on collection under certain conditions; waiver authority (a) In general Notwithstanding subsections (f) and (g) of section 1710 of this title, section 1722A(a) of this title, section 1725A of this title, or any other provision of law requiring an individual to make a copayment to the Secretary, the Secretary may not require a veteran to make any copayment for the receipt of hospital care or medical services under the laws administered by the Secretary after the end of the two-year period beginning on the date such veteran received such hospital care or medical services if the Secretary failed to provide the veteran notice\u2014 (1) of the copayment within applicable timeliness standards established by the Secretary; or (2) that the aggregate amount of copayments for such care or services the veteran owes to the Secretary is greater than the dollar amount described in paragraph (1) of subsection (b). (b) Dollar amount described (1) The dollar amount described in this paragraph is $2,000. (2) On the first day of each fiscal year beginning after the date of the enactment of the STRIVE Act of 2025, the Secretary shall, increase the dollar amount described in paragraph (1) by a percentage equal to the percentage by which the Consumer Price Index (all items, United States city average) increased during the previous fiscal year. In the event that such index does not increase during such period, the Secretary shall maintain the dollar amount in effect under paragraph (1) during the previous fiscal year. (c) Waiver authority The Secretary may waive the requirement for a veteran to make any copayment for the receipt of such hospital care or medical services in any case in which the Secretary determines such a waiver would be appropriate, without regard to whether the veteran submits to the Secretary a request for such waiver. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1722C the following new item:\n1722D. Copayments: prohibition on collection of under certain conditions; waiver authority. .\n#### 3. Extension of certain limits on payments of pension\nSection 5503(d)(7) of title 38, United States Code, is amended by striking November 30, 2031 and inserting February 29, 2032 .",
      "versionDate": "2025-11-07",
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
            "name": "Health care costs and insurance",
            "updateDate": "2025-08-08T15:16:10Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-08-08T15:16:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-24T18:11:56Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3812ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3812rh.xml"
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
      "title": "STRIVE Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-11-08T10:53:14Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Stop Troubling Retroactive Invoices for Veteran Expenses Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-11-08T10:53:14Z"
    },
    {
      "title": "STRIVE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STRIVE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Troubling Retroactive Invoices for Veteran Expenses Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to prohibit the collection of a health care copayment by the Secretary of Veterans Affairs from a veteran under certain conditions attributable to a failure of the Department of Veterans Affairs to process certain information within applicable timeliness standards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T06:18:20Z"
    }
  ]
}
```
