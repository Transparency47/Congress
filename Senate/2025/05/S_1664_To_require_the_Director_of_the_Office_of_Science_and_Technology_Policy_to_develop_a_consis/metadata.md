# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1664?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1664
- Title: RESEARCHER Act
- Congress: 119
- Bill type: S
- Bill number: 1664
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S2800-2801)
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S2800-2801)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1664",
    "number": "1664",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "RESEARCHER Act",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (Sponsor introductory remarks on measure: CR S2800-2801)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
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
        "item": [
          {
            "date": "2025-05-07T21:19:21Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-07T21:19:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "KS"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "CA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "DE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1664is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1664\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Padilla (for himself and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Director of the Office of Science and Technology Policy to develop a consistent set of policy guidelines for Federal research agencies to address financial instability of graduate researchers and postdoctoral researchers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Relieving Economic Strain to Enhance American Resilience and Competitiveness in Higher Education and Research Act or the RESEARCHER Act .\n#### 2. Policy guidelines for Federal research agencies to address financial instability of graduate researchers and postdoctoral researchers\n##### (a) Definition\nIn this section:\n**(1) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(2) Graduate researchers**\nThe term graduate researchers means individuals enrolled in a degree program leading to an advanced degree who receive stipends or other compensation to conduct research in any discipline at an institution of higher education that is a recipient of Federal funding.\n**(3) Postdoctoral researchers**\nThe term postdoctoral researchers means individuals in training-focused positions who have received a doctoral degree or equivalent and receive stipends or other compensation to conduct research in any discipline at an institution of higher education that is a recipient of Federal funding.\n##### (b) OSTP guidelines\n**(1) In general**\nNot later than 6 months after the date of enactment of this Act, the Director of the Office of Science and Technology Policy, in consultation with the National Science and Technology Council, the Committee on Science, Technology, Engineering, and Math Education of the National Science and Technology Council, the President\u2019s Council of Advisors on Science and Technology, institutions of higher education, graduate and postdoctoral organizations, and other relevant stakeholders, shall develop a consistent set of policy guidelines for Federal research agencies to address financial instability of graduate researchers and postdoctoral researchers.\n**(2) Requirements**\nIn developing the policy guidelines under paragraph (1), the Director of the Office of Science and Technology Policy shall include guidelines that address, to the extent practicable, the following:\n**(A)**\nOpportunities to increase stipends for graduate researchers and postdoctoral researchers, including indexing based on location.\n**(B)**\nAn additional consideration for increasing stipends for postdoctoral researchers conducting research in rural or underserved areas, or in States eligible to receive funding from the Established Program to Stimulate Competitive Research under section 113 of the National Science Foundation Authorization Act of 1988 ( 42 U.S.C. 1862g ), to support the recruitment and retention of researchers in such regions.\n**(C)**\nOpportunities to increase access to quality, affordable medical, dental, and vision care.\n**(D)**\nOpportunities to increase access to affordable housing and transportation.\n**(E)**\nOpportunities to reduce food insecurity.\n**(F)**\nOpportunities to address costs of caring for family members, including child care.\n**(3) Application**\n**(A) In general**\nThe Director of the Office of Science and Technology Policy shall encourage and monitor efforts of Federal research agencies to develop and implement policies based on the policy guidelines under paragraph (1).\n**(B) Federal research agency implementation**\nNot later than 6 months after receiving the policy guidelines under paragraph (1), the head of each Federal research agency shall\u2014\n**(i)**\ndevelop and implement policies with respect to financial instability of graduate researchers and postdoctoral researchers that are consistent with such policy guidelines; and\n**(ii)**\nbroadly disseminate such policies to current and potential recipients of research and development awards made by such agency.\n**(4) Updates**\nThe Director of the Office of Science and Technology Policy shall update the policy guidelines under paragraph (1) as the Director determines necessary.\n**(5) Report**\nNot later than 1 year after the date after the guidelines are submitted and every 5 years thereafter, the Director of the Office of Science and Technology Policy shall submit to the Committee on Commerce, Science, and Transportation and the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Science, Space, and Technology, the Committee on Education and Workforce, and Committee on Energy and Commerce of the House of Representatives, a report containing information relating to the following:\n**(A)**\nThe policy guidelines under paragraph (1).\n**(B)**\nProgress on the implementation of such guidelines by Federal research agencies.\n##### (c) Data collection\nThe Research and Development, Competition, and Innovation Act ( 42 U.S.C. 18901 et seq. ) is amended\u2014\n**(1)**\nin section 10314(b)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (D), by striking and after the semicolon;\n**(ii)**\nby redesignating subparagraph (E) as subparagraph (F); and\n**(iii)**\nby inserting after subparagraph (D) the following new subparagraph:\n(E) graduate researcher and postdoctoral researcher stipend amounts and financial instability (disaggregated, to the extent practicable, by demographics); and ; and\n**(B)**\nby adding at the end the following new paragraph:\n(5) Definitions In this subsection: (A) Institution of higher education The term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ). (B) Graduate researchers The term graduate researchers means individuals enrolled in a degree program leading to an advanced degree who receive stipends or other compensation to conduct research in any discipline at an institution of higher education that is a recipient of Federal funding. (C) Postdoctoral researchers The term postdoctoral researchers means individuals in training-focused positions who have received a doctoral degree or equivalent and receive stipends or other compensation to conduct research in any discipline at an institution of higher education that is a recipient of Federal funding. ; and\n**(2)**\nin paragraph (1) of section 10502(a), by inserting graduate and postdoctoral research stipend amounts (disaggregated, to the extent practicable, by demographics), before and awarded budget .\n##### (d) Data on financial instability of graduate researchers and postdoctoral researchers\nThe Director of the National Science Foundation shall make awards, on a competitive basis, to institutions of higher education or nonprofit organizations (or consortia of such institutions or organizations) to collect and analyze data on financial instability of graduate researchers and postdoctoral researchers (disaggregated, to the extent practicable, by demographics).\n##### (e) National Academies assessment\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Director of the National Science Foundation shall enter into an agreement with the National Academies of Sciences, Engineering, and Medicine to undertake a study and issue a report on the status of financial instability of graduate researchers and postdoctoral researchers. To the extent feasible, the study shall include an assessment (disaggregated, to the extent practicable, by demographics) at a minimum of the immediately preceding 5 years of the following:\n**(A)**\nStipends relative to average local medical, dental, and vision expenses.\n**(B)**\nStipends relative to average local housing and transportation costs.\n**(C)**\nStipends relative to average local food costs.\n**(D)**\nStipends relative to average local costs of caring for family members, including child care costs.\n**(2) Report**\nNot later than 2 years after the date on which the agreement between the Director of the National Science Foundation and the National Academies of Sciences, Engineering, and Medicine is entered into pursuant to paragraph (1), the National Academies of Sciences, Engineering, and Medicine shall submit to the Committee on Commerce, Science, and Transportation and the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Science, Space, and Technology, the Committee on Education and Workforce, and the Committee on Energy and Commerce of the House of Representatives a report containing the results of the assessment under such paragraph and recommendations relating thereto regarding how Federal agencies, Congress, institutions of higher education, and other relevant entities may address financial instability of graduate researchers and postdoctoral researchers.\n##### (f) GAO study\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Commerce, Science, and Transportation and the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Science, Space, and Technology, the Committee on Education and Workforce, and the Committee on Energy and Commerce of the House of Representatives a report that\u2014\n**(1)**\nassesses the degree to which Federal research agencies have implemented the policy guidelines under subsection (b) and the effectiveness of such implementation;\n**(2)**\nincludes recommendations on potential changes to practices and policies to improve such guidelines and such implementation; and\n**(3)**\nincludes recommendations on additional data collection and research needed to monitor progress on reducing financial instability of graduate researchers and postdoctoral researchers.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-04-29",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "3054",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RESEARCHER Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-29T15:15:26Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1664is.xml"
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
      "title": "RESEARCHER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RESEARCHER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Relieving Economic Strain to Enhance American Resilience and Competitiveness in Higher Education and Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the Office of Science and Technology Policy to develop a consistent set of policy guidelines for Federal research agencies to address financial instability of graduate researchers and postdoctoral researchers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:32Z"
    }
  ]
}
```
