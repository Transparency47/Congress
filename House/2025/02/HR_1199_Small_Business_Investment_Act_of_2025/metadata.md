# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1199?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1199
- Title: Small Business Investment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1199
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-12-05T21:56:55Z
- Update date including text: 2025-12-05T21:56:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1199",
    "number": "1199",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Small Business Investment Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:56:55Z",
    "updateDateIncludingText": "2025-12-05T21:56:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:02:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1199ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1199\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Kustoff introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the exclusion for gain from qualified small business stock.\n#### 1. Short title\nThis Act may be cited as the Small Business Investment Act of 2025 .\n#### 2. Phased increase in exclusion for gain from qualified small business stock\n##### (a) In general\nSection 1202(a)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 50 percent and inserting the applicable percentage , and\n**(2)**\nby striking held for more than 5 years and inserting held for at least 3 years .\n##### (b) Applicable percentage\nSection 1202(a) of such Code is amended by adding at the end the following new paragraph:\n(5) Applicable percentage Except as provided in paragraphs (3) and (4), the applicable percentage under paragraph (1) shall be determined under the following table: Years stock held: Applicable percentage: 3 years 50% 4 years 75% 5 years or more 100% .\n##### (c) Continued treatment as not item of tax preference\n**(1) In general**\nSection 57(a)(7) of such Code is amended by striking An amount and inserting In the case of stock acquired on or before the date of the enactment of the Creating Small Business Jobs Act of 2010, an amount .\n**(2) Conforming amendment**\nSection 1202(a)(4) of such Code is amended\u2014\n**(A)**\nby striking , and at the end of subparagraph (B) and inserting a period, and\n**(B)**\nby striking subparagraph (C).\n##### (d) Other conforming amendments\n**(1)**\nSection 1202(a)(4) of such Code is amended by inserting and before the date of the enactment of the Small Business Investment Act of 2025 after Act of 2010 .\n**(2)**\nParagraphs (3) and (4) of section 1202(a) of such Code are each amended by inserting held for more than 5 years and after In the case of qualified small business stock .\n**(3)**\nSection 1202(a)(3)(A) of such Code is amended to read as follows:\n(A) the applicable percentage under paragraph (1) shall be 75 percent, and ,\n**(4)**\nSection 1202(a)(4)(A) of such Code is amended to read as follows:\n(A) the applicable percentage under paragraph (1) shall be 100 percent, and .\n**(5)**\nSection 1202(b)(2) of such Code is amended by striking more than 5 years and inserting at least 3 years .\n**(6)**\nSection 1202(g)(2)(A) of such Code is amended by striking more than 5 years and inserting at least 3 years .\n**(7)**\nSection 1202(j)(1)(A) of such Code is amended by striking more than 5 years and inserting at least 3 years .\n##### (e) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to stock acquired after the date of the enactment of this Act.\n**(2) Continued treatment as not item of tax preference**\nThe amendment made by subsection (c) shall take effect as if included in the enactment of section 2011 the Creating Small Business Jobs Act of 2010.\n#### 3. Tacking holding period of convertible debt instruments\n##### (a) In general\nSection 1202(f) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B) and moving such subparagraphs (as so redesignated) 2 ems to the right,\n**(2)**\nby striking conversion of other stock .\u2014If any stock and inserting the following:\nconversion.\u2014 (1) Other stock If any stock , and\n**(3)**\nby adding at the end the following new paragraph:\n(2) Convertible debt instruments (A) In general If any stock in a corporation is acquired by the taxpayer, without recognition of gain, solely through the conversion of a qualified convertible debt instrument\u2014 (i) the stock so acquired shall be treated as qualified small business stock in the hands of the taxpayer, and (ii) the stock so acquired shall be treated as having been held during the period during which the qualified convertible debt instrument was held. (B) Qualified convertible debt instrument For purposes of this paragraph, the term qualified convertible debt instrument means any bond or other evidence of indebtedness\u2014 (i) which is originally issued by the corporation to the taxpayer, (ii) the issuer of which\u2014 (I) from issuance until conversion, is a qualified small business, and (II) during substantially all of the taxpayer\u2019s holding period of such bond or evidence of indebtedness, the corporation meets the active business requirements of subsection (e), and (iii) which is convertible into stock in the corporation. .\n##### (b) Effective date\nThe amendments made by this section shall apply to debt instruments originally issued after the date of the enactment of this Act.\n#### 4. Gain exclusion allowed with respect to qualified small business stock in corporation\n##### (a) In general\nSection 1202(c) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking C corporation in paragraphs (1) and inserting corporation , and\n**(2)**\nby striking and such corporation is a C corporation in paragraph (2)(A).\n##### (b) Qualified small business definition\nSection 1202(d)(1) of such Code is amended by striking which is a C corporation .\n##### (c) Clarification of aggregation rules applicable to S corporations\nSection 1202(d)(3) of such Code is amended by adding at the end the following new subparagraph:\n(C) Clarification with respect to S corporations Any determination of the members of a controlled group of corporations under this paragraph shall include taking into account any stock ownership in an S corporation. .\n##### (d) Treatment of passive losses\nSection 469(g)(1) of such Code is amended by adding at the end the following new subparagraph:\n(D) Certain dispositions of small business stock In the case a disposition any gain from which is excluded from gross income under section 1202, subparagraph (A) shall not apply. .\n##### (e) Special rules relating to S corporations\nSection 1202(e) of such Code is amended by adding at the end the following new paragraph:\n(9) Applied at S corporation level In the case of an S corporation, the requirements of this subsection shall be applied at the corporate level. .\n##### (f) Effective date\nThe amendments made by this section shall apply to stock acquired after the date of the enactment of this Act.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-02-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "695",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Small Business Investment Act of 2025",
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
        "updateDate": "2025-05-05T18:51:48Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1199ih.xml"
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
      "title": "Small Business Investment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Investment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modify the exclusion for gain from qualified small business stock.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:42Z"
    }
  ]
}
```
