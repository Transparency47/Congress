# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8532?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8532
- Title: VA Home Loan Affordability Act
- Congress: 119
- Bill type: HR
- Bill number: 8532
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-13T16:10:19Z
- Update date including text: 2026-05-13T16:10:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8532",
    "number": "8532",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "VA Home Loan Affordability Act",
    "type": "HR",
    "updateDate": "2026-05-13T16:10:19Z",
    "updateDateIncludingText": "2026-05-13T16:10:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
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
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:02:40Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "MI"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "VA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8532ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8532\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Mr. Van Orden (for himself, Mr. Bost , Mr. Barrett , Mrs. Kiggans of Virginia , and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to align elements of the housing loan program of the Department of Veterans Affairs with requirements of the Federal Housing Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Home Loan Affordability Act .\n#### 2. Alignment of housing loan program of the Department of Veterans Affairs with requirements of the Federal Housing Administration\n##### (a) Prohibition of requirement of third party verification of lender fees\nSection 3703(a)(2)(B) of title 38, United States Code, is amended\u2014\n**(1)**\nby inserting in regulations after Secretary may prescribe ; and\n**(2)**\nby adding at the end the following: In prescribing such regulations regarding fees paid by a veteran borrower to lender, the Secretary may not require documentation of such fees by a third party.\n##### (b) Refinancing of housing loans\n**(1) Authority to waive appraisal**\nSection 3709(a) of title 38, United States Code, is amended\u2014\n**(A)**\nby redesignating paragraphs (1) through (3) as subparagraphs (A) through (C), respectively;\n**(B)**\nby inserting (1) before Except ; and\n**(C)**\nby adding at the end the following new paragraph:\n(2) The Secretary may authorize the refinancing of a loan described in paragraph (1) without an appraisal. .\n**(2) Minimum interest rate for adjustable rate mortgage**\nSection 3709(b)(3) of title 38, United States Code, is amended by striking 200 basis points and inserting 75 basis points .\n##### (c) Expansion of guaranteed loans for condominiums\nSection 3710(a)(6) of title 38, United States Code, is amended, in subsection (a)(6), by striking , if such development or project is approved by the Secretary under criteria which the Secretary shall prescribe in regulations .\n##### (d) Maximum closing costs and seller fees for guaranteed loans\nSection 3710(b) of title 38, United States Code, is amended\u2014\n**(1)**\nin paragraph (7)(C)(ii), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (8), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following new paragraphs:\n(9) the closing costs actually paid by the veteran do not exceed 1.5 percent of the amount of the loan; and (10) the seller fees actually paid by the veteran do not exceed six percent of the outstanding balance of the loan. .\n##### (e) Regular prescription of debt-to-Income ratios\nSection 3710(g)(3)(A), of title 38, United States Code, is amended by inserting , reviewed and prescribed not less than once every two years, after debt-to-income ratios .\n##### (f) Minimum experience of an appraiser required\nSection 3731(a)(1) of title 38, United States Code, is amended by striking certification of an appropriate number of years and inserting a certificate or license issued by a State .\n##### (g) Review of appraisal minimum property requirements\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall\u2014\n**(1)**\nreview regulations prescribed under section 3710(b)(4) of title 38, United States Code, regarding the suitability of property; and\n**(2)**\nprescribe new such regulations that the Secretary determines appropriate.\n##### (h) Plan To modernize IT for housing loans\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans Affairs of the Senate and House of Representatives the plan of the Secretary to modernize the information technology used to administer housing loans under chapter 37 of title 38, United States Code.",
      "versionDate": "2026-04-27",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-13T16:10:19Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8532ih.xml"
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
      "title": "VA Home Loan Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Home Loan Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to align elements of the housing loan program of the Department of Veterans Affairs with requirements of the Federal Housing Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:48:46Z"
    }
  ]
}
```
