# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7107
- Title: Accountability for NYCHA Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7107
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-02-06T14:38:53Z
- Update date including text: 2026-02-06T14:38:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Financial Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7107",
    "number": "7107",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Accountability for NYCHA Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-06T14:38:53Z",
    "updateDateIncludingText": "2026-02-06T14:38:53Z"
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
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
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
          "date": "2026-01-15T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7107ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7107\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Lawler introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Inspector General of the Department of Housing and Urban Development to provide a report to the Congress on the non-compliance of the New York City Housing Authority, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accountability for NYCHA Act of 2026 .\n#### 2. Congressional findings\nThe Congress finds that\u2014\n**(1)**\nthe New York City Housing Authority (in this Act referred to as the Authority ) is the largest housing authority in the United States, providing housing for over 520,000 residents in over 177,000 apartments in the City of New York (in this Act referred to as the City );\n**(2)**\nthe Authority is a public housing agency that receives Federal financial assistance from the Department of Housing and Urban Development (in this Act referred to as the Department ) to administer its public housing program;\n**(3)**\nthe Authority is required to, among other things, provide decent, safe, and sanitary housing for the public housing residents of the City and comply with Federal law protecting children from the hazards of lead poisoning;\n**(4)**\non June 11, 2018, the United States filed a complaint in the United States District Court for the Southern District of New York (in this Act referred to as the Complaint ); which set forth the findings of the United States investigation, alleging, among other things, that the Authority had\u2014\n**(A)**\nroutinely failed to comply with lead-based paint safety regulations;\n**(B)**\nfailed to provide decent, safe, and sanitary housing, including with respect to the provision of heat and elevators and the control and treatment of mold and pests; and\n**(C)**\nrepeatedly misled the Department through false statements and deceptive practices;\n**(5)**\nin a Consent Decree executed June 11, 2018, the Authority made admissions regarding, among other things, deficiencies in physical conditions with respect to lead, mold, heating, elevators and pests and made untrue statements to the Department regarding the conditions of the Authority\u2019s properties and practices with regard to Public Housing Assessment System inspections;\n**(6)**\nbased on the Authority\u2019s misconduct as detailed in the Complaint, on January 31, 2019, the Secretary of Housing and Urban Development (in this Act referred to as the Secretary ) declared that the Authority is in substantial default within the meaning of section 6(j)(3)(A) of the United States Housing Act of 1937 ( 42 U.S.C. 1437d(j)(3)(A) );\n**(7)**\nthe Department did not take possession of the Authority or appoint a receiver, but instead entered into a voluntary agreement between the Authority, the Department, and the City on January 31, 2019, under which the Authority agreed to remedy noted deficiencies subject to the oversight of a Monitor appointed by the City;\n**(8)**\nas of the date of the enactment of this Act, the Authority has still fully not complied with the agreement, including the remedying of deficiencies or compliance with its obligations under Federal law;\n**(9)**\nthe Department and the United States Attorney\u2019s Office for the Southern District of New York have sought to extend the term of a Monitor over the Authority for an additional 5 years beginning in 2024 through 2029;\n**(10)**\non February 6, 2024, 70 NYCHA employees were charged by the Department of Justice on Federal bribery charges in the largest number of Federal bribery charges on a single day;\n**(11)**\nthe residents of housing provided by the Authority should not be required to wait five additional years for the Authority to provide decent, safe, and sanitary housing conditions, as is the Authority\u2019s most basic and necessary function under the law; and\n**(12)**\nthe Congress believes that it must provide additional oversight over the Authority, the Department, the City, and the Monitor in order to compel the Authority to fix the appalling conditions and other issues that lead to a declaration of substantial default under section 6(j)(3)(A) of the United States Housing Act of 1937.\n#### 3. Investigation and report to Congress\n##### (a) Investigation\nThe Inspector General of the Department of Housing and Urban Development shall conduct an investigation of the Authority, which shall include at a minimum\u2014\n**(1)**\ndetermining the status of the New York City Housing Authority\u2019s compliance with the agreement entered into between the Authority, the Department, and the City on January 31, 2019, including specific areas of deficiency and progress towards compliance;\n**(2)**\nconducting a review of actions taken by the Monitor over the Authority pursuant to such Agreement, including any gaps in oversight by the Monitor;\n**(3)**\nconducting a survey of the physical conditions of housing provided by the Authority for the City\u2019s residents;\n**(4)**\nconducting an examination of any waste, fraud, abuse and violations of Federal law committed by employees or contractors of the Authority; and\n**(5)**\nidentifying other priority issues and areas, as deemed necessary and appropriate by the Inspector General.\n##### (b) Report\nNot later than the expiration of the 180-day period beginning on the date of the enactment of this Act, the Inspector General shall provide to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate a report setting forth the findings of its investigation, a summary of actions the Department may take to compel the Authority to remedy deficiencies, and any other recommendations of the Inspector General.",
      "versionDate": "2026-01-15",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-02-06T14:38:52Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7107ih.xml"
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
      "title": "Accountability for NYCHA Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Accountability for NYCHA Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Inspector General of the Department of Housing and Urban Development to provide a report to the Congress on the non-compliance of the New York City Housing Authority, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T04:18:16Z"
    }
  ]
}
```
