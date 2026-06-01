# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4213?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4213
- Title: Data Center Water and Energy Transparency Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4213
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-15T14:38:04Z
- Update date including text: 2026-04-15T14:38:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S1616-1617)
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S1616-1617)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4213",
    "number": "4213",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
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
    "title": "Data Center Water and Energy Transparency Act of 2026",
    "type": "S",
    "updateDate": "2026-04-15T14:38:04Z",
    "updateDateIncludingText": "2026-04-15T14:38:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S1616-1617)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T22:37:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4213is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4213\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Durbin introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require data center operators to submit to States or the Administrator of the Environmental Protection Agency and the Secretaries of Energy and Agriculture reports on data center energy and water use, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Data Center Water and Energy Transparency Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Data center terms**\nThe terms data center and data center operator have the meanings given those terms in section 453(a) of the Energy Independence and Security Act of 2007 ( 42 U.S.C. 17112(a) ).\n**(3) Energy use**\nThe term energy use , with respect to data centers, means the total quantity of electricity and other forms of energy consumed on site by that data center, as measured in kilowatt-hours.\n**(4) Power usage effectiveness**\nThe term power usage effectiveness has the meaning given the term in ISO/IEC 30134\u20132:2026 of the International Organization for Standardization (or a successor standard).\n**(5) Secretaries**\nThe term Secretaries means the Secretary of Energy and the Secretary of Agriculture.\n**(6) State**\nThe term State means\u2014\n**(A)**\neach of the several States;\n**(B)**\na territory of the United States;\n**(C)**\nthe Federated States of Micronesia;\n**(D)**\nthe Republic of the Marshall Islands;\n**(E)**\nthe Republic of Palau;\n**(F)**\nan Indian tribe included on the list most recently published by the Secretary of the Interior under section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ); and\n**(G)**\nthe District of Columbia.\n**(7) Unit of local government**\nThe term unit of local government means any county, parish, city, town, township, village, or other general purpose political subdivision of a State with the power to levy taxes, expend Federal, State, and local funds, and exercise governmental powers.\n**(8) Water usage effectiveness**\nThe term water usage effectiveness has the meaning given the term in ISO/IEC 30134\u20139:2022 of the International Organization for Standardization (or a successor standard).\n**(9) Water use**\nThe term water use , with respect to a data center, means the total amount of water consumed on-site by a data center, including water used for cooling, as measured in gallons.\n#### 3. Data center mandatory reporting and information requirement\n##### (a) Data collection\n**(1) Report to State**\n**(A) In general**\nBeginning not later than 1 year after the date of enactment of this Act but subject to paragraph (2), each data center operator with 1 or more data centers in a State shall submit to that State an annual report that, with respect to each data center in the State with a peak demand of not less than 25 megawatts operated by that data center operator, describes\u2014\n**(i)**\non-site energy use and water use for the preceding calendar year, including\u2014\n**(I)**\ntotal energy use during each month of that calendar year;\n**(II)**\nif the data center relies on behind-the-meter power generation, the method to generate that power;\n**(III)**\ntotal water use and the source of that water during each month of that calendar year; and\n**(IV)**\nannual average power usage effectiveness and water usage effectiveness;\n**(ii)**\nprojected on-site energy use and water use for not less than the following 5 calendar years, which shall include proposals for reducing the energy use and water use of the data center and the increases in efficiency that are anticipated to result from those proposals; and\n**(iii)**\nsuch other information as the State may require.\n**(B) Form**\nA data center operator shall submit a report under subparagraph (A) in such form and in such manner as the applicable State may require.\n**(C) Fees authorized**\nA State may, in requiring the reports described in this paragraph, assess fees on data center operators to support data collection under this paragraph.\n**(2) Report to Administrator and Secretaries**\n**(A) In general**\nIf a State does not have a program to collect the information described in clauses (i) and (ii) of paragraph (1)(A)\u2014\n**(i)**\nthe State shall inform the Administrator and the Secretaries jointly; and\n**(ii)**\na data center operator with data centers in such a State shall submit to the Administrator and Secretaries jointly a report that, with respect to each data center in such a State with a peak demand of not less than 25 megawatts operated by that data center operator, describes\u2014\n**(I)**\nthe information described in those clauses; and\n**(II)**\nsuch other information as the Administrator and Secretaries may jointly require.\n**(B) Form**\nA data center operator shall submit a report under subparagraph (A) in such form and in such manner as the Administrator and Secretaries may jointly require.\n**(3) Reports to local governments**\nA report to a State or the Administrator and the Secretaries jointly under paragraph (1) or (2) shall be made available to an affected unit of local government on request and, if applicable, in compliance with any program established by the State for the collection of those reports.\n##### (b) Reports on prospective and expanded data centers\n**(1) Report to State**\n**(A) In general**\nSubject to paragraph (2), each person seeking to construct a data center with a projected energy use of not less than 25 megawatts and each data center operator seeking to expand a data center with a projected energy use of not less than 25 megawatts shall submit to the State in which the new or expanded data center would operate a report that describes\u2014\n**(i)**\nas applicable\u2014\n**(I)**\nthe projected energy use and water use and the sources of energy and water of the new data center during the first 5 calendar years after the data center begins operation; or\n**(II)**\nthe projected increase in energy use and water use as a result of the expansion of a data center during the first 5 calendar years after completion of the expansion; and\n**(ii)**\nproposals for reducing the energy use and water use of the data center and the increases in efficiency that are anticipated to result from those proposals.\n**(B) Form**\nA report submitted under subparagraph (A) shall be submitted in such form and in such manner as the applicable State may require.\n**(2) Report to Administrator and Secretaries**\n**(A) In general**\nIf a State does not have a program to collect the information described in paragraph (1)(A)\u2014\n**(i)**\nthe State shall inform the Administrator and the Secretaries jointly; and\n**(ii)**\na person seeking to construct a data center and each data center operator seeking to expand a data center in such a State shall submit to the Administrator and the Secretaries jointly a report that describes, with respect to the proposed data center or the expansion of the data center, the information described in that paragraph.\n**(B) Form**\nA person or data center operator shall submit a report under subparagraph (A) in such form and in such manner as the Administrator and Secretaries may jointly require.\n**(3) Reports to local governments**\nA report to a State or the Administrator and the Secretaries jointly under paragraph (1) or (2) shall be made available to an affected unit of local government on request and, if applicable, in compliance with any program established by the State for the collection of those reports.\n##### (c) Aggregated reports\n**(1) Reports from States**\n**(A) In general**\nEach State that receives a report under subsection (a)(1) or (b)(1) shall submit to the Administrator and the Secretaries jointly an annual report that describes the data collected pursuant to all such reports submitted to the State under subsection (a)(1) or (b)(1), as applicable, during the previous year in such a manner as may be required jointly by the Administrator and the Secretaries.\n**(B) Anonymized data**\nThe reports submitted under subparagraph (A) shall only include anonymized and aggregated information.\n**(2) Public report**\nThe Administrator and the Secretaries shall jointly make publicly available on an annual basis a report that\u2014\n**(A)**\ndescribes\u2014\n**(i)**\nusing information collected from the reports under subsections (a)(2) and (b)(2) and paragraph (1)(A), the aggregated total energy use and water use of data centers in the United States, by region, during the calendar year covered by the report;\n**(ii)**\nregional impacts of data centers on water and electricity rates for consumers and communities;\n**(iii)**\nthe environmental impacts resulting from the operation of data centers, including\u2014\n**(I)**\nwater and energy sources, supply, quality, and reliability impacts on consumers and communities; and\n**(II)**\nother direct or indirect impacts; and\n**(iv)**\nrecommendations for best practices to limit the impacts described in clauses (ii) and (iii);\n**(B)**\nincludes, based on the reports received by the Administrator and the Secretaries jointly under subsections (a)(2) and (b)(2) and paragraph (1)(A) for the calendar year covered by the report, the aggregated projection of energy use and water use by data centers for the 5 years following that calendar year; and\n**(C)**\ndoes not include any information that the Administrator and the Secretaries jointly determine is proprietary.\n##### (d) Rulemaking\n**(1) Federal authority**\nThe Administrator and the Secretaries may jointly promulgate such regulations as may be necessary to carry out this section.\n**(2) State authority**\nA State may promulgate such regulations in accordance with the laws of the State as may be necessary to carry out this section.\n##### (e) Enforcement\n**(1) State enforcement**\nIf a State establishes a program for collecting data pursuant to subsection (a)(1) and (b)(1), the State may issue fines and otherwise engage in other enforcement activities to comply with the requirements of this Act and applicable State laws.\n**(2) Federal enforcement**\n**(A) In general**\nSubject to paragraph (2), the Administrator and the Secretaries shall jointly fine a data center operator that negligently violates a requirement of subsection (a)(2) or (b)(2) $20,000 for each day that the data center operator is in violation of that requirement.\n**(B) Inflation adjustment**\nOn the date that is 3 years after the date of enactment of this Act, and every 3 years thereafter, the Administrator and the Secretaries shall jointly adjust the amount described in subparagraph (A) to reflect changes for the 36-month period ending the preceding November 30 in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor.\n#### 4. Fees\nThe Administrator and the Secretaries shall jointly assess fees on data center operators that submit a report under subsection (a)(2) or (b)(2) of section 3 in an amount necessary to carry out this Act and may, without further appropriation, use the amounts collected to carry out those subsections.",
      "versionDate": "2026-03-25",
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-15T14:38:04Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4213is.xml"
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
      "title": "Data Center Water and Energy Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T02:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Data Center Water and Energy Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T02:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require data center operators to submit to States or the Administrator of the Environmental Protection Agency and the Secretaries of Energy and Agriculture reports on data center energy and water use, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T02:33:18Z"
    }
  ]
}
```
