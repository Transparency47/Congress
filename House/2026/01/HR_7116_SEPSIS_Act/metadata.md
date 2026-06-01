# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7116
- Title: SEPSIS Act
- Congress: 119
- Bill type: HR
- Bill number: 7116
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-05-12T08:05:36Z
- Update date including text: 2026-05-12T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7116",
    "number": "7116",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "N000188",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Norcross, Donald [D-NJ-1]",
        "lastName": "Norcross",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "SEPSIS Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:36Z",
    "updateDateIncludingText": "2026-05-12T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:00:35Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "NJ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "DC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7116ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7116\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Norcross (for himself and Mr. Kean ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish programs to reduce rates of sepsis.\n#### 1. Short title\nThis Act may be cited as the Securing Enhanced Programs, Systems, and Initiatives for Sepsis Act or the SEPSIS Act .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\n1,700,000 individuals in the United States are diagnosed with sepsis annually and 350,000 individuals in the United States are killed by sepsis each year.\n**(2)**\nThere is a need for increased Federal investment in research related to sepsis to build on research supported by the National Institutes of Health, including research with a pediatric focus supported by the Eunice Kennedy Shriver National Institute of Child Health and Human Development.\n**(3)**\nThe infectious disease workforce, which plays a key role in reducing the burden of sepsis, needs additional support to recruit and retain health care professionals engaged in infection prevention and related patient care.\n**(4)**\nSepsis is one of the most expensive conditions to treat in hospitals in the United States, with high spending compounded by frequent hospital re-admissions, including 1 in 5 patient re-admissions within 30 days of discharge and 1 in 3 patient re-admissions within 180 days of discharge.\n**(5)**\nAccording to the Centers for Disease Control and Prevention, 80 percent of sepsis cases begin outside of the hospital.\n**(6)**\nMost sepsis fatalities are preventable with early recognition, diagnosis, and treatment.\n**(7)**\nThe sepsis protocols for hospitals in New York State, called Rory\u2019s Regulations for Rory Staunton who died from preventable, treatable sepsis at 12 years of age, have been proven to save lives through rapid identification and treatment of sepsis.\n**(8)**\nProviders and public health experts should study and learn from Rory\u2019s Regulations to find ways to end preventable deaths from sepsis on a national scale.\n#### 3. Sepsis programs\nTitle III of the Public Health Service Act ( 42 U.S.C. 241 et seq. ) is amended by inserting after section 317V the following:\n317W. Sepsis programs (a) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention (referred to in this section as the Director ), shall maintain a sepsis team for purposes of\u2014 (1) leading an education campaign on best practices for addressing sepsis in hospitals, such as the practices outlined in the Hospital Sepsis Program Core Elements set forth by the Centers for Disease Control and Prevention; (2) improving data collection on pediatric sepsis; (3) sharing information with the Administrator of the Centers for Medicare & Medicaid Services to inform the development and implementation of sepsis quality measures to improve outcomes for patients; (4) updating data elements with respect to sepsis used by the United States Core Data for Interoperability, in coordination with the heads of other relevant agencies and offices of the Department of Health and Human Services, including the National Coordinator for Health Information Technology and the Director of the Office of Public Health Data, Surveillance, and Technology; (5) facilitating efforts across the Department of Health and Human Services to develop outcome measures with respect to sepsis; and (6) carrying out other activities related to sepsis, as the Director determines appropriate. (b) Report on development of outcome measures Not later than 1 year after the date of enactment of the Securing Enhanced Programs, Systems, and Initiatives for Sepsis Act , the Director shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report on the development and implementation of outcome measures for sepsis, for both adult and pediatric populations, that take into consideration the social and clinical factors that affect the likelihood a patient will develop sepsis. (c) Annual briefing on sepsis activities Not later than 1 year after the date of enactment of the Securing Enhanced Programs, Systems, and Initiatives for Sepsis Act , and annually thereafter, the Director shall present to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a briefing on\u2014 (1) aggregate data on the adoption by hospitals of sepsis best practices, including the Hospital Sepsis Program Core Elements, as reported by hospitals to the Director, using the hospital sepsis program assessment tool of the Centers for Disease Control and Prevention and State sepsis reporting requirements; (2) rates of pediatric sepsis and efforts to reduce cases of pediatric sepsis, including how the Hospital Sepsis Program Core Elements can be effective at supporting efforts to reduce cases of pediatric sepsis; (3) the coordination of sepsis reduction efforts across the Department of Health and Human Services; (4) in partnership with the Director of the Agency for Healthcare Research and Quality, an evaluation of the impact of the Hospital Sepsis Program Core Elements on quality of care for patients; (5) data sharing from the National Healthcare Safety Network with other agencies and offices of the Department of Health and Human Services with respect to sepsis; and (6) a report on the latest datasets on sepsis, as provided to the Director by the Director of the Agency for Healthcare Research and Quality. (d) Honor roll program (1) In general The Secretary may establish a voluntary program for recognizing hospitals that maintain effective sepsis programs or improve their sepsis programs over time, including in the areas of early detection, effective treatment, and overall progress in the reduction of the burden of sepsis. (2) Applications; selection In carrying out paragraph (1), the Secretary shall\u2014 (A) solicit applications from hospitals; and (B) establish public benchmarks by which the Secretary will select hospitals for recognition under such paragraph, including with respect to each area described in such paragraph. (e) Authorization of appropriations To carry out this section, there are authorized to be appropriated $20,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2026-01-15",
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
        "actionDate": "2025-06-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S3207-3208)"
      },
      "number": "1929",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SEPSIS Act",
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
        "name": "Health",
        "updateDate": "2026-02-05T18:17:14Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7116ih.xml"
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
      "title": "SEPSIS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T11:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEPSIS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Enhanced Programs, Systems, and Initiatives for Sepsis Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish programs to reduce rates of sepsis.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:51Z"
    }
  ]
}
```
