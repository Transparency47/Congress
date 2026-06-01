# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8871?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8871
- Title: DME Scammer Prevention Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8871
- Origin chamber: House
- Introduced date: 2026-05-19
- Update date: 2026-05-22T08:07:25Z
- Update date including text: 2026-05-22T08:07:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 25 - 19.
- Latest action: 2026-05-19: Introduced in House

## Actions

- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Introduced in House
- 2026-05-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 25 - 19.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8871",
    "number": "8871",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "DME Scammer Prevention Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:25Z",
    "updateDateIncludingText": "2026-05-22T08:07:25Z"
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
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 25 - 19.",
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
            "date": "2026-05-21T15:08:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-19T16:00:40Z",
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
          "date": "2026-05-19T16:00:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8871ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8871\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2026 Mr. Bean of Florida introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to promote Medicare program integrity with respect to certain medical equipment and supplies.\n#### 1. Short title\nThis Act may be cited as the DME Scammer Prevention Act of 2026 .\n#### 2. Promoting Medicare program integrity with respect to certain medical equipment and supplies\n##### (a) Electronic submission of claims by all providers and suppliers\nSection 1862(h) of the Social Security Act ( 42 U.S.C. 1395y(h) ) is amended\u2014\n**(1)**\nin paragraph (1)(A)(ii), by striking the entity and inserting except in the case of claims for specified items (as defined in paragraph (3)), the entity ; and\n**(2)**\nby adding at the end the following new paragraph:\n(3) For purposes of paragraph (1)(A)(ii), the term specified items means medical equipment and supplies (as defined in section 1834(j)(5)) furnished on or after January 1, 2027, that are included on the Master List described in section 1834(a)(23). .\n##### (b) Submission of claims within 90 days\nSection 1842(b)(3) of the Social Security Act ( 42 U.S.C. 1395u(b)(3) ) is amended\u2014\n**(1)**\nin subparagraph (B), in the flush matter following clause (ii), by inserting (or, in the case of claims for applicable items, the period ending 90 days after such date of service) after date of service ; and\n**(2)**\nin the flush matter following subparagraph (L)\u2014\n**(A)**\nin the sixth sentence\u2014\n**(i)**\nby inserting or end of the 90-day period specified in such subparagraph (as applicable) after close of the following calendar year ; and\n**(ii)**\nby inserting or end of such period (as applicable) after close of such year ;\n**(B)**\nin the ninth sentence, by inserting or 90-day period (as applicable) after 1 calendar year period ; and\n**(C)**\nby adding at the end the following new sentence: For purposes of subparagraph (B), the term applicable items means specified items (as defined in section 1862(h)(3)), other than any such item that is included on the Required Face-to-Face Encounter and Written Order Prior to Delivery List described in section 410.38(c)(8) of title 42, Code of Federal Regulations (or a successor regulation) or on the Required Prior Authorization List described in section 414.234(c)(1) of title 42 of such Code (or a successor regulation) or for which payment is made on a monthly rental basis. .\n##### (c) Report\n**(1) In general**\nNot later than January 1, 2030, the Comptroller General of the United States shall submit to Congress a report on the technology used by medicare administrative contractors to screen claims for specified items to identify errors or indicators of potential waste, fraud, or abuse. Such report shall include, with respect to the 1-year period beginning on January 1, 2027\u2014\n**(A)**\nan examination of\u2014\n**(i)**\nthe total number of such claims submitted during such period for which payment was initially denied on the basis of such screening technology; and\n**(ii)**\nthe total number of claims so denied for which payment was ultimately made; and\n**(B)**\nan examination of the extent to which the use of such screening technology (taking into account the amendments made by subsections (a) and (b)) assists in the identification of\u2014\n**(i)**\nsuspicious claims or aberrant billing practices that may be indicative of improper payments; and\n**(ii)**\nthe basis of claims denials.\n**(2) Definitions**\nIn this subsection:\n**(A) Medicare administrative contractor**\nThe term medicare administrative contractor has the meaning given such term in section 1874A(a)(3) of the Social Security Act ( 42 U.S.C. 1395kk\u20131(a)(3) ).\n**(B) Specified items**\nThe term specified items has the meaning given such term in section 1862(h)(3) of the Social Security Act, as added by subsection (a).",
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8871ih.xml"
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
      "title": "DME Scammer Prevention Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DME Scammer Prevention Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-20T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to promote Medicare program integrity with respect to certain medical equipment and supplies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-20T08:19:23Z"
    }
  ]
}
```
