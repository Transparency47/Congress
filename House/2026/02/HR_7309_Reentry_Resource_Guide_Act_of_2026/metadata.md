# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7309?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7309
- Title: Reentry Resource Guide Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7309
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-02-25T16:48:40Z
- Update date including text: 2026-02-25T16:48:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-02: Introduced in House

## Actions

- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7309",
    "number": "7309",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Reentry Resource Guide Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-25T16:48:40Z",
    "updateDateIncludingText": "2026-02-25T16:48:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7309ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7309\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Mr. Cleaver introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish a pilot program to develop, expand, and maintain digital community resource guides to advance the reentry efforts of individuals returning to their communities after incarceration.\n#### 1. Short title\nThis Act may be cited as the Reentry Resource Guide Act of 2026 .\n#### 2. Pilot program\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall establish a pilot program to make grants to eligible applicants to develop, expand, and maintain digital community resource guides of statewide resources to advance the reentry efforts of individuals returning to their communities after incarceration. Such guides shall\u2014\n**(1)**\nbe a comprehensive list detailing names and contact information for statewide resources;\n**(2)**\nbe sortable by regions within the State for easier accessibility;\n**(3)**\nbe available for download; and\n**(4)**\nbe appropriate, relevant, and available, with special considerations for\u2014\n**(A)**\nemployment services;\n**(B)**\nhousing services;\n**(C)**\nlocal crisis lines;\n**(D)**\noutreach agencies;\n**(E)**\nlocal shelters;\n**(F)**\nshower and restrooms;\n**(G)**\nclothing and storage;\n**(H)**\ncooling and warming stations for extreme temperature or weather conditions;\n**(I)**\nfood pantries;\n**(J)**\nhot meals;\n**(K)**\nidentification assistance services;\n**(L)**\ntransportation services;\n**(M)**\nrelocation services;\n**(N)**\nlegal services;\n**(O)**\neducation services;\n**(P)**\ngovernment services;\n**(Q)**\naddiction counseling and treatment for gambling;\n**(R)**\naddiction counseling and treatment for substance abuse services;\n**(S)**\nharm reduction services;\n**(T)**\nmental and health services and referrals;\n**(U)**\nmedical and dental services;\n**(V)**\ndomestic violence shelters;\n**(W)**\nservices for living with HIV or AIDS;\n**(X)**\ndisability services;\n**(Y)**\nseniors services;\n**(Z)**\nfamily services;\n**(AA)**\nveteran services;\n**(BB)**\nyouth and young people services;\n**(CC)**\ngovernment services; and\n**(DD)**\ninformation and referral services.\n#### 3. Application; grant term\n##### (a) Application\nA State may apply for a grant under this section by submitting an application including\u2014\n**(1)**\na strategy for identifying community resources;\n**(2)**\nidentification of relevant statewide resources, their physical locations, and contact information;\n**(3)**\nidentification of the entity or personnel responsible for the creation and management of the guide;\n**(4)**\nidentification of where the guide will be accessible; and\n**(5)**\na plan for promotion of awareness of the resource guides within the prison and returning population.\n##### (b) Grant term\nA grant under this section shall be for a term of 3 years.\n#### 4. Use of funds\nAmounts provided as grants under this Act may be used for\u2014\n**(1)**\nproject planning and community engagement;\n**(2)**\nproject implementation;\n**(3)**\noperational costs including costs of startup or expansion of the existing system, outreach, and language translation;\n**(4)**\nemployee salary associated with the guide's expansion, creation, and maintenance; and\n**(5)**\nmaintenance of the digital site the guide is listed.\n#### 5. Reporting\n##### (a) Grantees\nEach grantee shall submit an annual report to AG that details specific uses of the grant funds, and the outcome of the program.\n##### (b) Attorney General\nAfter the termination of the pilot program, the Attorney General shall submit to Congress a report including an evaluation detailing the implementation of, outcome of, and impact of the program on reduction of recidivism and overall successful reentry.\n#### 6. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act $8,000,000 for each of fiscal years 2027 through 2030.",
      "versionDate": "2026-02-02",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-25T16:48:40Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7309ih.xml"
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
      "title": "Reentry Resource Guide Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reentry Resource Guide Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a pilot program to develop, expand, and maintain digital community resource guides to advance the reentry efforts of individuals returning to their communities after incarceration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T07:48:29Z"
    }
  ]
}
```
