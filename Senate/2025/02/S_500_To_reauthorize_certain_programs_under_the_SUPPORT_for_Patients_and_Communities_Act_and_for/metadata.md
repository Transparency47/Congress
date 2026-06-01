# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/500
- Title: CAREER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 500
- Origin chamber: Senate
- Introduced date: 2025-02-10
- Update date: 2026-04-03T19:59:00Z
- Update date including text: 2026-04-03T19:59:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-10: Introduced in Senate
- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-10: Introduced in Senate

## Actions

- 2025-02-10 - IntroReferral: Introduced in Senate
- 2025-02-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/500",
    "number": "500",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M000355",
        "district": "",
        "firstName": "Mitch",
        "fullName": "Sen. McConnell, Mitch [R-KY]",
        "lastName": "McConnell",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "CAREER Act of 2025",
    "type": "S",
    "updateDate": "2026-04-03T19:59:00Z",
    "updateDateIncludingText": "2026-04-03T19:59:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T23:10:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TN"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s500is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 500\nIN THE SENATE OF THE UNITED STATES\nFebruary 10, 2025 Mr. McConnell (for himself, Mr. Hagerty , and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo reauthorize certain programs under the SUPPORT for Patients and Communities Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Comprehensive Addiction Recovery through Effective Employment and Reentry Act of 2025 or the CAREER Act of 2025 .\n#### 2. Reauthorization of the CAREER Act; treatment, recovery, and workforce support grants\n##### (a) In general\nSection 7183 of the SUPPORT for Patients and Communities Act ( 42 U.S.C. 290ee\u20138 ) is amended\u2014\n**(1)**\nin the section heading, by inserting ; treatment, recovery, and workforce support grants after CAREER Act ;\n**(2)**\nin subsection (b), by inserting each before for a period ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by striking the rates described in paragraph (2) and inserting the average rates for calendar years 2018 through 2022 described in paragraph (2) ; and\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) Rates The rates described in this paragraph are the following: (A) The highest age-adjusted average rates of drug overdose deaths for calendar years 2018 through 2022 based on data from the Centers for Disease Control and Prevention, including, if necessary, provisional data for calendar year 2022. (B) The highest average rates of unemployment for calendar years 2018 through 2022 based on data provided by the Bureau of Labor Statistics. (C) The lowest average labor force participation rates for calendar years 2018 through 2022 based on data provided by the Bureau of Labor Statistics. ;\n**(4)**\nin subsection (g)\u2014\n**(A)**\nin each of paragraphs (1) and (3), by redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and adjusting the margins accordingly;\n**(B)**\nby redesignating paragraphs (1) through (3) as subparagraphs (A) through (C), respectively, and adjusting the margins accordingly;\n**(C)**\nin the matter preceding subparagraph (A) (as so redesignated), by striking An entity and inserting the following:\n(1) In general An entity ; and\n**(D)**\nby adding at the end the following:\n(2) Transportation services An entity receiving a grant under this section may use not more than 5 percent of the funds for providing transportation for individuals to participate in an activity supported by a grant under this section, which transportation shall be to or from a place of work or a place where the individual is receiving vocational education or job training services or receiving services directly linked to treatment of or recovery from a substance use disorder. (3) Limitation The Secretary may not require an entity to, or give priority to an entity that plans to, use the funds of a grant under this section for activities that are not specified in this subsection. ;\n**(5)**\nin subsection (i)(2), by inserting , which shall include employment and earnings outcomes described in subclauses (I) and (III) of section 116(b)(2)(A)(i) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3141(b)(2)(A)(i) ) with respect to the participation of such individuals with a substance use disorder in programs and activities funded by the grant under this section after subsection (g) ;\n**(6)**\nin subsection (j)\u2014\n**(A)**\nin paragraph (1), by inserting for grants awarded prior to the date of enactment of the Comprehensive Addiction Recovery through Effective Employment and Reentry Act of 2025 after grant period under this section ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking 2 years after submitting the preliminary report required under paragraph (1) and inserting September 30, 2030 ; and\n**(ii)**\nin subparagraph (A), by striking (g)(3) and inserting (g)(1)(C) ; and\n**(7)**\nin subsection (k), by striking $5,000,000 for each of fiscal years 2019 through 2023 and inserting $12,000,000 for each of fiscal years 2026 through 2030 .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ; 132 Stat. 3894) is amended by striking the item relating to section 7183 and inserting the following:\nSec. 7183. CAREER Act; treatment, recovery, and workforce support grants. .\n#### 3. Reauthorization of the CAREER Act; Recovery Housing Pilot Program\n##### (a) In general\nSection 8071 of the SUPPORT for Patients and Communities Act ( 42 U.S.C. 5301 note; Public Law 115\u2013271 ) is amended\u2014\n**(1)**\nby striking the section heading and inserting CAREER Act; Recovery Housing Pilot Program ;\n**(2)**\nin subsection (a), by striking through 2023 and inserting through 2030 ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking not later than 60 days after the date of enactment of this Act and inserting not later than 60 days after the date of enactment of the Comprehensive Addiction Recovery through Effective Employment and Reentry Act of 2025 ; and\n**(B)**\nin paragraph (2)(B)(i)\u2014\n**(i)**\nin subclause (I)\u2014\n**(I)**\nby striking for calendar years 2013 through 2017 ; and\n**(II)**\nby inserting for calendar years 2018 through 2022 after rates of unemployment ;\n**(ii)**\nin subclause (II)\u2014\n**(I)**\nby striking for calendar years 2013 through 2017 ; and\n**(II)**\nby inserting for calendar years 2018 through 2022 after participation rates ; and\n**(iii)**\nby striking subclause (III) and inserting the following:\n(III) The highest age-adjusted average rates of drug overdose deaths for calendar years 2018 through 2022 based on data from the Centers for Disease Control and Prevention, including, if necessary, provisional data for calendar year 2022. ; and\n**(4)**\nin subsection (f), by striking For the 2-year period following the date of enactment of this Act, the and inserting The .\n##### (b) Conforming amendment\nSubtitle F of title VIII of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ; 132 Stat. 4095) is amended by striking the subtitle heading and inserting the following:\nF CAREER Act; Recovery Housing Pilot Program .\n##### (c) Clerical amendments\nThe table of contents in section 1(b) of the SUPPORT for Patients and Communities Act ( Public Law 115\u2013271 ; 132 Stat. 3894) is amended\u2014\n**(1)**\nby striking the item relating to subtitle F of title VIII and inserting the following:\nSubtitle F\u2014CAREER Act; Recovery Housing Pilot Program ;\nand\n**(2)**\nby striking the item relating to section 8071 and inserting the following:\nSec. 8071. CAREER Act; Recovery Housing Pilot Program. .",
      "versionDate": "2025-02-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-18",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2121",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SUPPORT for Patients and Communities Reauthorization Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-01",
        "text": "Became Public Law No: 119-44."
      },
      "number": "2483",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SUPPORT for Patients and Communities Reauthorization Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
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
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2026-01-23T18:31:52Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-01-23T18:32:06Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2026-01-23T18:32:16Z"
          },
          {
            "name": "Labor market",
            "updateDate": "2026-01-23T18:32:01Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2026-01-23T18:31:57Z"
          },
          {
            "name": "Unemployment",
            "updateDate": "2026-01-23T18:32:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-12T16:37:03Z"
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
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s500is.xml"
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
      "title": "CAREER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CAREER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Comprehensive Addiction Recovery through Effective Employment and Reentry Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize certain programs under the SUPPORT for Patients and Communities Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:35Z"
    }
  ]
}
```
