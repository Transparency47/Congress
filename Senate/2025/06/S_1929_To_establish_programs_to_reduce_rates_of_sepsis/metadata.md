# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1929?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1929
- Title: SEPSIS Act
- Congress: 119
- Bill type: S
- Bill number: 1929
- Origin chamber: Senate
- Introduced date: 2025-06-03
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in Senate
- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S3207-3208)
- Latest action: 2025-06-03: Introduced in Senate

## Actions

- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S3207-3208)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1929",
    "number": "1929",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "SEPSIS Act",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S3207-3208)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-03",
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
            "date": "2025-06-03T16:20:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-03T16:20:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "ME"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NJ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MN"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CT"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "AK"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1929is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1929\nIN THE SENATE OF THE UNITED STATES\nJune 3, 2025 Mr. Schumer (for himself, Ms. Collins , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish programs to reduce rates of sepsis.\n#### 1. Short title\nThis Act may be cited as the Securing Enhanced Programs, Systems, and Initiatives for Sepsis Act or the SEPSIS Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\n1,700,000 individuals in the United States are diagnosed with sepsis annually and 350,000 individuals in the United States are killed by sepsis each year.\n**(2)**\nThere is a need for increased Federal investment in research related to sepsis to build on research supported by the National Institutes of Health, including research with a pediatric focus supported by the Eunice Kennedy Shriver National Institute of Child Health and Human Development.\n**(3)**\nThe infectious disease workforce, which plays a key role in reducing the burden of sepsis, needs additional support to recruit and retain health care professionals engaged in infection prevention and related patient care.\n**(4)**\nSepsis is one of the most expensive conditions to treat in hospitals in the United States, with high spending compounded by frequent hospital re-admissions, including 1 in 5 patient re-admissions within 30 days of discharge and 1 in 3 patient re-admissions within 180 days of discharge.\n**(5)**\nAccording to the Centers for Disease Control and Prevention, 80 percent of sepsis cases begin outside of the hospital.\n**(6)**\nMost sepsis fatalities are preventable with early recognition, diagnosis, and treatment.\n**(7)**\nThe sepsis protocols for hospitals in New York State, called Rory\u2019s Regulations for Rory Staunton who died from preventable, treatable sepsis at 12 years of age, have been proven to save lives through rapid identification and treatment of sepsis.\n**(8)**\nProviders and public health experts should study and learn from Rory\u2019s Regulations to find ways to end preventable deaths from sepsis on a national scale.\n#### 3. Sepsis programs\nTitle III of the Public Health Service Act ( 42 U.S.C. 241 et seq. ) is amended by inserting after section 317V the following:\n317W. Sepsis programs (a) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention (referred to in this section as the Director ), shall maintain a sepsis team for purposes of\u2014 (1) leading an education campaign on best practices for addressing sepsis in hospitals, such as the practices outlined in the Hospital Sepsis Program Core Elements set forth by the Centers for Disease Control and Prevention; (2) improving data collection on pediatric sepsis; (3) sharing information with the Administrator of the Centers for Medicare & Medicaid Services to inform the development and implementation of sepsis quality measures to improve outcomes for patients; (4) updating data elements with respect to sepsis used by the United States Core Data for Interoperability, in coordination with the heads of other relevant agencies and offices of the Department of Health and Human Services, including the National Coordinator for Health Information Technology and the Director of the Office of Public Health Data, Surveillance, and Technology; (5) facilitating efforts across the Department of Health and Human Services to develop outcome measures with respect to sepsis; and (6) carrying out other activities related to sepsis, as the Director determines appropriate. (b) Report on development of outcome measures Not later than 1 year after the date of enactment of the Securing Enhanced Programs, Systems, and Initiatives for Sepsis Act , the Director shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report on the development and implementation of outcome measures for sepsis, for both adult and pediatric populations, that take into consideration the social and clinical factors that affect the likelihood a patient will develop sepsis. (c) Annual briefing on sepsis activities Not later than 1 year after the date of enactment of the Securing Enhanced Programs, Systems, and Initiatives for Sepsis Act , and annually thereafter, the Director shall present to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a briefing on\u2014 (1) aggregate data on the adoption by hospitals of sepsis best practices, including the Hospital Sepsis Program Core Elements, as reported by hospitals to the Director, using the hospital sepsis program assessment tool of the Centers for Disease Control and Prevention and State sepsis reporting requirements; (2) rates of pediatric sepsis and efforts to reduce cases of pediatric sepsis, including how the Hospital Sepsis Program Core Elements can be effective at supporting efforts to reduce cases of pediatric sepsis; (3) the coordination of sepsis reduction efforts across the Department of Health and Human Services; (4) in partnership with the Director of the Agency for Healthcare Research and Quality, an evaluation of the impact of the Hospital Sepsis Program Core Elements on quality of care for patients; (5) data sharing from the National Healthcare Safety Network with other agencies and offices of the Department of Health and Human Services with respect to sepsis; and (6) a report on the latest datasets on sepsis, as provided to the Director by the Director of the Agency for Healthcare Research and Quality. (d) Honor roll program (1) In general The Secretary may establish a voluntary program for recognizing hospitals that maintain effective sepsis programs or improve their sepsis programs over time, including in the areas of early detection, effective treatment, and overall progress in the reduction of the burden of sepsis. (2) Applications; selection In carrying out paragraph (1), the Secretary shall\u2014 (A) solicit applications from hospitals; and (B) establish public benchmarks by which the Secretary will select hospitals for recognition under such paragraph, including with respect to each area described in such paragraph. (e) Authorization of appropriations To carry out this section, there are authorized to be appropriated $20,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-06-03",
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
        "actionDate": "2026-01-15",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7116",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SEPSIS Act",
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
        "name": "Health",
        "updateDate": "2025-06-18T14:14:54Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1929is.xml"
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
      "title": "SEPSIS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SEPSIS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing Enhanced Programs, Systems, and Initiatives for Sepsis Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish programs to reduce rates of sepsis.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T04:18:17Z"
    }
  ]
}
```
