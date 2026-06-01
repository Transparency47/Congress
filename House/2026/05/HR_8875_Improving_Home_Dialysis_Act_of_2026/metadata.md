# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8875?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8875
- Title: Improving Home Dialysis Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8875
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-22T08:08:55Z
- Update date including text: 2026-05-22T08:08:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 28 - 13.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 28 - 13.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8875",
    "number": "8875",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Improving Home Dialysis Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:55Z",
    "updateDateIncludingText": "2026-05-22T08:08:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 28 - 13.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
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
      "actionDate": "2026-05-19",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-19",
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
            "date": "2026-05-21T15:04:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-19T16:03:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-19T16:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8875ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8875\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Mrs. Miller of West Virginia introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to include certain additional services as self-care home dialysis support services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Improving Home Dialysis Act of 2026 .\n#### 2. Including certain additional services as self-care home dialysis support services under the Medicare program\n##### (a) In general\nSection 1881(b)(9) of the Social Security Act ( 42 U.S.C. 1395rr(b)(9) ) is amended\u2014\n**(1)**\nin subparagraph (C), by striking and at the end;\n**(2)**\nby redesignating subparagraph (D) as subparagraph (F);\n**(3)**\nby inserting after subparagraph (C) the following new subparagraphs:\n(D) beginning January 1, 2028, staff-assisted home dialysis respite care furnished to a patient in the place of residence used as such patient\u2019s home (other than a skilled nursing facility or a nursing facility (as defined in section 1919(a))); (E) beginning January 1, 2028, renal mental health services furnished to a patient in the place of residence used as such patient\u2019s home (other than a skilled nursing facility or a nursing facility (as defined in section 1919(a))); and ; and\n**(4)**\nby adding at the end the following flush matter:\nFor purposes of subparagraph (D), the term staff-assisted home dialysis respite care means dialysis services furnished by qualified personnel to a patient dialyzing at home who is temporarily unable to competently dialyze at home independently during the 30-day period beginning on the first day that the patient initiates home dialysis (or, in the case of a patient whose temporary inability to competently dialyze is attributable to a physical limitation, at any time). For purposes of the preceding sentence, the term qualified personnel means a registered nurse, a licensed practical nurse, a certified patient care technician, or another qualified medical professional specified by the Secretary, who meets requirements (as determined by the Secretary) that ensure competency in patient care and modality usage, including completing training specific to staff-assisted home dialysis respite care as specified by the Secretary. For purposes of subparagraph (E), the term renal mental health services means services described in section 494.90(a)(6) of title 42, Code of Federal Regulations (or a successor regulation), furnished to a patient dialyzing at home during the 60-day period beginning on the first day that the patient initiates home dialysis by an individual who meets the standard specified in section 494.140(d) of title 42, Code of Federal Regulations (or a successor regulation). .\n##### (b) Payment adjustments for certain self-care home dialysis support services\n**(1) In general**\nSection 1881(b)(14) of the Social Security Act ( 42 U.S.C. 1395rr(b)(14) ) is amended\u2014\n**(A)**\nin subparagraph (D)\u2014\n**(i)**\nin clause (iii), by striking and at the end;\n**(ii)**\nby redesignating clause (iv) as clause (vi); and\n**(iii)**\nby inserting after clause (iii) the following new clauses:\n(iv) shall include a payment adjustment for staff-assisted home dialysis respite care (as described in paragraph (9)(D)) in accordance with subparagraph (J); (v) shall include a payment adjustment for renal mental health services (as described in paragraph (9)(E)) in accordance with subparagraph (K); and ; and\n**(B)**\nby adding at the end the following new subparagraphs:\n(J) (i) For purposes of subparagraph (D)(iv), subject to clause (ii), a payment adjustment shall be made for each session of staff-assisted home dialysis respite care (as described in paragraph (9)(D)) furnished during a year equal to the amount of the add-on per treatment adjustment for home and self-dialysis training furnished in 2025 (or, in the case of such care that is not furnished in a rural area (as defined for purposes of such subparagraph), 75 percent of such amount). (ii) In no case may a payment adjustment under subparagraph (D)(iv) be made for staff-assisted home dialysis respite care furnished to an individual\u2014 (I) for more than 20 sessions in a calendar year; or (II) on a day when such individual was not dialyzing at home. (iii) Any payment adjustment under subparagraph (D)(iv) for staff-assisted home dialysis respite care shall not be made in a budget neutral manner. (K) (i) For purposes of subparagraph (D)(v), subject to clause (ii), a payment adjustment shall be made for each session of renal mental health services (as described in paragraph (9)(E)) furnished during a year equal to 50 percent (or 25 percent, in the case of such services that are not furnished in a rural area (as defined for purposes of subparagraph (D))) of the amount of the add-on per treatment adjustment for home and self-dialysis training furnished in 2025. (ii) In no case may a payment adjustment under subparagraph (D)(v) be made for renal mental health services furnished to an individual\u2014 (I) for more than 4 sessions occurring during the 60-day period beginning on the first day that the individual initiates home dialysis; or (II) on a day when such individual was not dialyzing at home. (iii) Any payment adjustment under subparagraph (D)(v) for renal mental health services shall not be made in a budget neutral manner. .\n**(2) Conforming amendment**\nSection 1834(r)(1) of the Social Security Act ( 42 U.S.C. 1395m(r)(1) ) is amended by striking subparagraph (D)(iv)(II) and inserting subparagraph (D)(vi)(II) .",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8875ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Home Dialysis Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "title": "Improving Home Dialysis Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to include certain additional services as self-care home dialysis support services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:19:37Z"
    }
  ]
}
```
