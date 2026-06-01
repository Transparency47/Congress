# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4449?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4449
- Title: Strengthening Educator Workforce Data Act
- Congress: 119
- Bill type: S
- Bill number: 4449
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-18T20:01:48Z
- Update date including text: 2026-05-18T20:01:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2173-2174)
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2173-2174)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4449",
    "number": "4449",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Strengthening Educator Workforce Data Act",
    "type": "S",
    "updateDate": "2026-05-18T20:01:48Z",
    "updateDateIncludingText": "2026-05-18T20:01:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2173-2174)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T16:59:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4449is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4449\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Durbin (for himself, Ms. Hirono , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo strengthen Federal data collection regarding the teacher and principal workforce.\n#### 1. Short title\nThis Act may be cited as the Strengthening Educator Workforce Data Act .\n#### 2. Civil rights data collection on the educator workforce\n##### (a) Mandatory educator workforce data collection\nIn carrying out the civil rights data collection required under section 203(c)(1) of the Department of Education Organization Act ( 20 U.S.C. 3413(c)(1) ), the Assistant Secretary for Civil Rights of the Department shall, as part of the data collection, collect and publish the data described in subsection (b) on the educator workforce with respect to teachers and principals.\n##### (b) Metrics\n**(1) In general**\nA civil rights data collection described in subsection (a) shall include the following metrics from each local educational agency and public elementary school or secondary school that is required to respond to such data collection:\n**(A) Principal data**\nFor each local educational agency, the following data regarding principals employed at public elementary schools and secondary schools served by the local educational agency:\n**(i)**\nThe number of full-time principals employed.\n**(ii)**\nIncluding the year of the data collection\u2014\n**(I)**\nthe median number of years of principal experience of full-time principals employed; and\n**(II)**\nthe years of experience of the full-time principals employed, based on the following categories:\n**(aa)**\nLess than 1 year of principal experience.\n**(bb)**\nAt least 1 year but less than 3 years of principal experience.\n**(cc)**\nAt least 3 years but less than 7 years of principal experience.\n**(dd)**\nAt least 7 years but less than 15 years of principal experience.\n**(ee)**\n15 or more years of principal experience.\n**(B) Teacher data**\nFor each local educational agency and public elementary school or secondary school, the following data regarding teachers employed at all public elementary schools and secondary schools served by a local educational agency, and each such school, respectively:\n**(i)**\nThe number of full-time teachers employed.\n**(ii)**\nIncluding the year of the data collection, but excluding student teaching and similar teaching preparation experiences\u2014\n**(I)**\nthe median number of years of teaching experience of full-time teachers employed; and\n**(II)**\nthe years of experience of the full-time teachers employed, based on the following categories:\n**(aa)**\nLess than 1 year of teaching experience.\n**(bb)**\nAt least 1 year but less than 2 years of teaching experience.\n**(cc)**\nAt least 2 years but less than 5 years of teaching experience.\n**(dd)**\nAt least 5 years but less than 10 years of teaching experience.\n**(ee)**\nAt least 10 years but less than 20 years of teaching experience.\n**(ff)**\n20 or more years of teaching experience.\n**(iii)**\nThe number of full-time teachers employed who meet all State licensing and certification requirements.\n**(iv)**\nThe number of full-time teachers employed who do not meet all State licensing and certification requirements.\n**(v)**\nThe numbers of full-time teachers employed who meet all State license, certificate, and endorsement requirements in each of the following:\n**(I)**\nMathematics.\n**(II)**\nScience.\n**(III)**\nEnglish as a second language.\n**(IV)**\nSpecial education.\n**(2) Disaggregation and cross-tabulation**\nThe Secretary shall collect the data described in paragraph (1) in a manner that allows the disaggregation and cross-tabulation of each data category (including each subcategory) described in such paragraph by race, ethnicity, and sex, subject to subsection (d).\n##### (c) Reporting requirements\n**(1) Special report**\nUpon the conclusion of each civil rights data collection that includes the data required under subsection (b), the Secretary, acting through the Assistant Secretary for Civil Rights of the Department, shall prepare a special report regarding the educator workforce.\n**(2) Contents**\nThe report required under paragraph (1) shall\u2014\n**(A)**\nbe accessible through the website of the Office for Civil Rights of the Department;\n**(B)**\ninclude information on\u2014\n**(i)**\nfor each State, the total number of principals in the educator workforce, as calculated in the most recent civil rights data collection that includes the data required under subsection (b), based on a summary of the data collected in accordance with this section; and\n**(ii)**\nfor each State, the total number of teachers in the educator workforce, as calculated in such data collection, based on a summary of the data collected in accordance with this section; and\n**(C)**\nfor each category described in subparagraph (B), present in an easily accessible manner, such as through percentages or a graph or other visual representation, the\u2014\n**(i)**\ndisaggregated results based on race, ethnicity, and sex; and\n**(ii)**\nthe disaggregated results based on the years of experience categories under subparagraph (A)(ii)(II) or (B)(ii)(II) of subsection (b)(1), as applicable.\n**(3) Access to data**\nThe Secretary shall make the underlying data used for the report under paragraph (1) accessible to the public through the website of the Office for Civil Rights of the Department.\n##### (d) Data privacy\nIn carrying out data collection, disaggregation, cross-tabulation, and reporting in accordance with this section and under section 203(c)(1) of the Department of Education Organization Act ( 20 U.S.C. 3413(c)(1) ), the Assistant Secretary for Civil Rights of the Department shall coordinate with the Chief Privacy Officer of the Department to ensure that teacher and principal privacy is protected and that individually identifiable information about teachers and principals remains confidential.\n##### (e) Definitions\nIn this section:\n**(1) ESEA definitions**\nThe terms Department , elementary school , local educational agency , secondary school , and State have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Teacher**\nThe term teacher means an individual employed as a teacher, including a preschool teacher, at a public elementary school or secondary school.\n##### (f) Applicability\nThis section shall apply with respect to each civil rights data collection required under section 203(c)(1) of the Department of Education Organization Act that begins on or after the date of enactment of this Act.",
      "versionDate": "2026-04-30",
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
        "actionDate": "2026-04-30",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "8636",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Strengthening Educator Workforce Data Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-05-18T19:57:03Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4449is.xml"
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
      "title": "Strengthening Educator Workforce Data Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T02:38:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Educator Workforce Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to strengthen Federal data collection regarding the teacher and principal workforce.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:38Z"
    }
  ]
}
```
