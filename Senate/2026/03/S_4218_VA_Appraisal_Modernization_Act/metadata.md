# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4218?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4218
- Title: VA Appraisal Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 4218
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-09T16:45:09Z
- Update date including text: 2026-04-09T16:45:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4218",
    "number": "4218",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "VA Appraisal Modernization Act",
    "type": "S",
    "updateDate": "2026-04-09T16:45:09Z",
    "updateDateIncludingText": "2026-04-09T16:45:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-03-26T16:28:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "MT"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4218is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4218\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Ms. Duckworth (for herself, Mr. Sheehy , and Mr. Banks ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to address appraisal fees for housing loans guaranteed by the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Appraisal Modernization Act .\n#### 2. Appraisal fees for Department of Veterans Affairs home loans\n##### (a) In general\nChapter 37 of title 38, United States Code, is amended by inserting after section 3731 the following new section:\n3731A. Appraisal fees (a) Definitions In this section: (1) Appraisal fee The term appraisal fee means the compensation paid to an appraiser for conducting an appraisal of property in connection with a loan guaranteed, insured, or made under this chapter. (2) High-demand county The term high-demand county means a county designated as a high-demand county under subsection (c). (3) Remote county The term remote county means a county designated as a remote county under subsection (c). (b) Annual inflation adjustment (1) Baseline Not later than 180 days after the date of the enactment of the VA Appraisal Modernization Act , the Secretary shall establish appraisal fees for purposes of this chapter. (2) Adjustment On January 1, 2027, and annually thereafter, the Secretary shall adjust the appraisal fees established under paragraph (1) to reflect the percentage of the increase, if any, in the purchase price of homes during the previous year, as determined by the quarterly purchase-only House Price Index published by the Federal Housing Finance Agency, rounded to the nearest $25. (3) Publication; notice The Secretary shall\u2014 (A) publish the appraisal fees established under this subsection on the publicly available website of the Department of Veterans Affairs; and (B) directly notify the appraisers on the list developed and maintained under section 3731(a)(3) of this title of such fees. (c) Designation of high-Demand counties and remote counties (1) High-demand counties (A) In general The Secretary shall designate a county as a high-demand county for purposes of this section if\u2014 (i) during the 90-day period preceding the date on which the designation is made\u2014 (I) the average time to complete an appraisal in the county exceeded the timeliness standard established under section 3731 of this title by more than three business days; or (II) more than 15 percent of appraisal assignments in the county were unassigned for five or more business days due to insufficient appraiser availability; or (ii) the Secretary determines, based on data analysis and market conditions, that demand for appraisals in the county substantially exceeds available appraiser capacity. (B) List; updates The Secretary shall\u2014 (i) maintain a list of high-demand counties designated under subparagraph (A); and (ii) on a quarterly basis, review and update such list. (2) Remote counties (A) In general The Secretary shall designate a county as a remote county for purposes of this section if\u2014 (i) there are fewer than five appraisers on the list developed and maintained under section 3731(a)(3) of this title within 30 miles of the county's geographic center; (ii) the average distance traveled by an appraiser to complete an assignment in the county is greater than 40 miles one way; or (iii) the Secretary determines that the county is characterized by low appraiser density relative to loan volume. (B) List; updates The Secretary shall\u2014 (i) maintain a list of remote counties designated under subparagraph (A); and (ii) on a quarterly basis, review and update such list. (d) Appraisal fees in high-Demand counties (1) In general On January 1, 2027, and annually thereafter, the Secretary shall increase the appraisal fee for appraisals made in high-demand counties to not less than 125 percent of the appraisal fee established under subsection (b). (2) Increase In carrying out paragraph (1), the Secretary may increase the appraisal fee for appraisals made in a high-demand county to not more than 150 percent of the appraisal fee established under subsection (b) if the county has been designated as a high-demand county for four quarters or more. (e) Mileage reimbursement (1) In general For any appraisal made for purposes of this chapter in a high-demand county or remote county, the Secretary shall reimburse the appraiser for mileage at the rate prescribed by the Administrator of General Services under section 5707(b) of title 5 for use on official business of privately owned automobiles. (2) Mileage In this subsection, the term mileage means the round trip distance in miles between the appraiser\u2019s place of business and the subject property. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 3731 the following new item:\n3731A. Appraisal fees. .\n#### 3. Report and study\n##### (a) Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committee on Finance of the Senate and the Committee on Ways and Means of the House of Representatives a report that includes the following:\n**(1)**\nAn estimation of\u2014\n**(A)**\nthe effects of section 3731A of title 38, United States Code, as added by section 2, on government expenditures over time;\n**(B)**\nthe impact of such section on the number of appraisers who join the appraisal network of the Department of Veterans Affairs;\n**(C)**\nthe impact of such section on completion times for appraisals in high-demand counties; and\n**(D)**\nthe impact of such section on the use of housing loans guaranteed, insured, or made under chapter 37 of title 38, United States Code.\n**(2)**\nRecommendations to prevent fraud, waste, and abuse in the implementation of such section.\n##### (b) Study\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall\u2014\n**(1)**\nconduct on a study on the feasibility and advisability of\u2014\n**(A)**\nprocuring contracts for home appraisers in areas where supply cannot meet demand; and\n**(B)**\nrestructuring the appraisal process of the Department of Veterans Affairs to more closely mirror the appraisal process for loans insured by the Federal Housing Administration; and\n**(2)**\nsubmit to Congress, and make publicly available, a report on the results of such study.",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in Senate"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-09T16:45:09Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4218is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "VA Appraisal Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VA Appraisal Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to address appraisal fees for housing loans guaranteed by the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:29Z"
    }
  ]
}
```
