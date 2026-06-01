# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1191
- Title: Studying NEPA’s Impact on Projects Act
- Congress: 119
- Bill type: S
- Bill number: 1191
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-12-19T12:03:16Z
- Update date including text: 2025-12-19T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1191",
    "number": "1191",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Studying NEPA\u2019s Impact on Projects Act",
    "type": "S",
    "updateDate": "2025-12-19T12:03:16Z",
    "updateDateIncludingText": "2025-12-19T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T19:27:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1191is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1191\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Curtis (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the National Environmental Policy Act of 1969 to require the Council on Environmental Quality to publish an annual report on environmental reviews and causes of action based on alleged non-compliance with that Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Studying NEPA\u2019s Impact on Projects Act .\n#### 2. CEQ annual report on NEPA\u2019s impact on projects\n##### (a) In general\nSection 201 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4341 ) is amended to read as follows:\n201. CEQ annual report (a) Title I definitions In this section, the terms categorical exclusion , cooperating agency , Council , environmental assessment , environmental impact statement , participating Federal agency , lead agency , and major Federal action have the meanings given those terms in section 111. (b) Report required Beginning on July 1, 2025, the Council shall annually publish on the website of the Council, and submit to the Committee on Environment and Public Works of the Senate and the Committee on Natural Resources of the House of Representatives, a report on\u2014 (1) each cause of action based on alleged non-compliance with this Act that was active during the period beginning on June 1 of the preceding year and ending on June 1 of the current year (referred to in this subsection as the covered year ), which shall identify\u2014 (A) with respect to each cause of action\u2014 (i) the defendant lead agency and the lead plaintiff; and (ii) (I) the court in which the cause of action was brought; and (II) any court to which a decision on the cause of action was appealed; (B) the number of causes of action, disaggregated by the defendant lead agency; (C) the alleged basis for each cause of action, disaggregated by type; and (D) the status and outcome, if applicable, of each cause of action, including whether\u2014 (i) the cause of action resulted in the major Federal action being reversed; (ii) the defendant lead agency was allowed to move forward with the major Federal action; (iii) the court issued a ruling directing the defendant lead agency to take additional measures to be in compliance with this Act; (iv) the lead plaintiff and the defendant lead agency entered into a settlement agreement; (v) the cause of action is still active; and (vi) the lead plaintiff received an award, including an award of costs pursuant to section 2412 of title 28, United States Code; (2) the length of environmental impact statements and environmental assessments prepared pursuant to sections 102(2)(C) and 106(b)(2), respectively, during the covered year, which shall include\u2014 (A) the average and median page count of each draft and final environmental impact statement and environmental assessment (including the appendix) published in the Federal Register during that covered year, including the page counts disaggregated by quartiles; (B) the number of draft and final environmental impact statements and environmental assessments published in the Federal Register during that covered year, disaggregated by defendant lead agency and subagency, as applicable; and (C) a description of trends in average and median page counts of draft and final environmental impact statements and environmental assessments published in the Federal Register during that covered year as compared to prior reports published by the Council; (3) the total cost to prepare the environmental impact statements and environmental assessments described in paragraph (2), including\u2014 (A) the full-time equivalent personnel hour costs, contractor costs, and other direct costs of the lead agency that prepared the environmental impact statement or environmental assessment; and (B) if practicable, and noted where not practicable, the costs incurred by cooperating agencies, participating Federal agencies, applicants, and contractors; (4) the timelines to complete environmental impact statements pursuant to section 102(2)(C) during the covered year, which shall include\u2014 (A) with respect to each major Federal action commenced during that covered year, the date on which, as applicable\u2014 (i) the project sponsor submitted an application for any permit or other authorization for the project; (ii) the lead agency began scoping for the project; (iii) the notice of intent to prepare the environmental impact statement was published in the Federal Register; (iv) the draft environmental impact statement was published in the Federal Register; (v) the final environmental impact statement was published in the Federal Register; (vi) the record of decision was published in the Federal Register; and (vii) the lead agency provided to the project sponsor notice to proceed on the project; (B) the average and median publication timelines during that covered year for each document described in subparagraph (A); (C) a description of trends in completion times during that covered year for those documents as compared to prior reports published by the Council; and (D) the number of Federal actions evaluated in each document described in subparagraph (A) during that covered year; and (5) a comprehensive list of categorical exclusions listed in the implementing regulations for this Act of each Federal agency, which shall identify\u2014 (A) the total number of categorical exclusions listed in those regulations; and (B) the total number of categorical exclusions established, adopted, or revised by each Federal agency during the covered year. (c) Format (1) Definition of covered sector In this subsection, the term covered sector means any of the following sectors: (A) Aviation and space. (B) Broadband. (C) Carbon capture and sequestration. (D) Conventional energy production. (E) Renewable energy production. (F) Electricity transmission. (G) Manufacturing. (H) Mining. (I) Pipelines. (J) Ports and waterways. (K) Surface transportation. (L) Information technology infrastructure. (M) Water resources. (N) Forestry. (O) Any other sector, as determined by the Council. (2) Disaggregation The information included in each report required under subsection (b) shall be disaggregated by the type of project and covered sector. (d) Public availability of data The Council shall publish with each report published under subsection (b) the underlying data used to prepare the report and include any citations or other information necessary for the public to locate records relating to the court proceedings for any cause of action described in paragraph (1) of that subsection. .\n##### (b) Conforming amendment\nSection 204 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4344 ) is amended by striking paragraph (1) and inserting the following:\n(1) to prepare the report required under section 201; .",
      "versionDate": "2025-03-27",
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
        "updateDate": "2025-05-01T17:34:41Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1191is.xml"
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
      "title": "Studying NEPA\u2019s Impact on Projects Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Studying NEPA\u2019s Impact on Projects Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Environmental Policy Act of 1969 to require the Council on Environmental Quality to publish an annual report on environmental reviews and causes of action based on alleged non-compliance with that Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:51Z"
    }
  ]
}
```
