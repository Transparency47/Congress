# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6676?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6676
- Title: State Industrial Competitiveness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6676
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-01-08T15:12:18Z
- Update date including text: 2026-01-08T15:12:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6676",
    "number": "6676",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "T000469",
        "district": "20",
        "firstName": "Paul",
        "fullName": "Rep. Tonko, Paul [D-NY-20]",
        "lastName": "Tonko",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "State Industrial Competitiveness Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T15:12:18Z",
    "updateDateIncludingText": "2026-01-08T15:12:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:00:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6676ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6676\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Tonko introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide financial assistance to States and Indian Tribes for the development, implementation, improvement, or expansion of a flex-tech energy program to enhance manufacturing competitiveness, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the State Industrial Competitiveness Act of 2025 .\n#### 2. State flex-tech energy program\n##### (a) In general\nPart D of title III of the Energy Policy and Conservation Act ( 42 U.S.C. 6321 et seq. ) is amended by adding at the end the following:\n367. Flex-tech energy program to enhance manufacturing competitiveness (a) Financial assistance Subject to the availability of appropriations, upon request from the State energy agency of a State that has in effect an approved State energy conservation plan under this part, or an Indian Tribe, the Secretary shall provide financial assistance to such State energy agency or Indian Tribe to be used for the development, implementation, improvement, or expansion of a flex-tech energy program described in subsection (b) to enhance manufacturing competitiveness. (b) Flex-Tech energy program elements (1) In general A flex-tech energy program may include\u2014 (A) provision of technical and administrative assistance to manufacturers through qualified engineering firms, as determined by the State energy agency or Indian Tribe; (B) provision of financial assistance to manufacturers\u2014 (i) for energy studies of manufacturing facilities that are conducted by qualified engineering firms; and (ii) to support the implementation of the measures and recommendations identified in energy studies conducted pursuant to clause (i), including the design, acquisition, installation, testing, operation, maintenance, and repair of energy- and water-using systems, resiliency-related measures, emissions reduction-related measures, utility cost savings measures, and measures related to advanced manufacturing technologies and artificial intelligence; and (C) reporting on monitoring, tracking, and success metrics of the program. (2) Studies An energy study of a manufacturing facility conducted pursuant to paragraph (1)(B) may include\u2014 (A) an evaluation of the energy-using systems of the facility, including evaluation of the performance of such systems relative to design intent, operational needs of the facility and its occupants, and operation and maintenance procedures; (B) an evaluation of emissions related to the facility, including greenhouse gas emissions, and recommendations on sustainability planning and practices; (C) an evaluation of potential energy efficiency, water efficiency, greenhouse gas emissions mitigation, and load reduction measures for the facility; (D) an evaluation of potential on-site energy measures, including grid-interactive efficiency systems, combined heat and power, industrial heat pumps, efficient compressed air systems, energy storage, energy management systems, renewable thermal systems, and electrification or other forms of fuel switching; (E) recommendations on the use of new technologies by the applicable manufacturer; and (F) detailed estimates of potential implementation costs, operating cost savings, energy savings, emissions reductions, and simple payback periods, for measures and recommendations identified in such study. (3) Qualified engineering firms A State energy agency or Indian Tribe administering a flex-tech energy program shall maintain and regularly update a publicly available list of qualified engineering firms that are approved by the State energy agency or Indian Tribe to provide assistance to manufacturers pursuant to this section. (c) Funding (1) Allocation Except as provided in paragraph (2), to the extent practicable, the Secretary shall allocate funding made available to carry out this section in accordance with the formula used for distribution of Federal financial assistance provided pursuant to this part to States that have in effect an approved State energy conservation plan under this part. (2) Indian Tribes The Secretary shall set aside and distribute not less than 5 percent of amounts made available for each fiscal year to carry out this section to provide financial assistance\u2014 (A) to Indian Tribes; or (B) directly to manufacturers located in Indian Country or, in the case of Alaska, an Alaska Native Village Statistical Area, as identified by the U.S. Census Bureau, for energy studies and implementation of the measures and recommendations identified in such energy studies, as described in subsection (b)(1)(B). (3) Use of funds (A) Energy studies; administrative expenses A State energy agency or Indian Tribe that receives financial assistance pursuant to this section for a fiscal year may not\u2014 (i) use more than 50 percent of such financial assistance for energy studies; (ii) use more than 50 percent of such financial assistance to support the implementation of recommendations from such energy studies; and (iii) use more than 10 percent of such financial assistance for administrative expenses, including for outreach and technical assistance. (B) Individual manufacturing facility A State energy agency that receives financial assistance pursuant to this section for a fiscal year may not use more than the greater of $100,000 or 5 percent of such financial assistance with respect to an individual manufacturing facility. (4) Supplement Financial assistance provided to a State energy agency or Indian Tribe pursuant to this section shall be used to supplement, not supplant, any Federal, State, or other funds otherwise made available to such State under this part. (5) Financing To the extent practicable, a State energy agency or Indian Tribe shall implement a flex-tech energy program described in subsection (b) using funding provided under this Act, public financing, private financing, or any other sources of funds. (d) Technical assistance (1) In general Upon request of a State energy agency or Indian Tribe, the Secretary shall provide information and technical assistance in the development, implementation, improvement, or expansion of a flex-tech energy program described in subsection (b). (2) Inclusions Technical assistance provided pursuant to paragraph (1) may include program design options to, with respect to manufacturers that employ fewer than 500 full-time equivalent employees at a manufacturing facility\u2014 (A) meet the needs of such manufacturers; and (B) encourage the use of advanced manufacturing processes by such manufacturers, including use of additive manufacturing, advanced sensors and controls, techniques to reduce embedded emissions, and advanced composite materials. (e) Definitions In this section: (1) Indian Country The term Indian Country means\u2014 (A) all land within the limits of any Indian reservation under the jurisdiction of the United States Government, notwithstanding the issuance of any patent, and, including rights-of-way running through the reservation; (B) all dependent Indian communities within the borders of the United States whether within the original or subsequently acquired territory thereof, and whether within or without the limits of a State; and (C) all Indian allotments, the Indian titles to which have not been extinguished, including rights-of-way running through the same. (2) Indian Tribe The term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). (3) State energy agency The term State energy agency has the meaning given such term in section 391(10). .\n##### (b) Conforming amendment\nThe table of contents for the Energy Policy and Conservation Act is amended by adding after the item related to section 366 the following:\nSec. 367. Flex-tech energy program to enhance manufacturing competitiveness. .\n##### (c) Authorization of appropriations\nSection 365(f) of the Energy Policy and Conservation Act ( 42 U.S.C. 6325(f) ) is amended by adding at the end the following:\n(3) Flex-tech energy program In addition to the authorization of appropriations under paragraph (1), for the purposes of carrying out section 367, there are authorized to be appropriated $100,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-12-11",
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
        "name": "Energy",
        "updateDate": "2026-01-08T15:12:18Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6676ih.xml"
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
      "title": "State Industrial Competitiveness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State Industrial Competitiveness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide financial assistance to States and Indian Tribes for the development, implementation, improvement, or expansion of a flex-tech energy program to enhance manufacturing competitiveness, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:20Z"
    }
  ]
}
```
