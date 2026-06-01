# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8124
- Title: STOP Suicide Act
- Congress: 119
- Bill type: HR
- Bill number: 8124
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-05-20T08:08:43Z
- Update date including text: 2026-05-20T08:08:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8124",
    "number": "8124",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000606",
        "district": "8",
        "firstName": "Jamie",
        "fullName": "Rep. Raskin, Jamie [D-MD-8]",
        "lastName": "Raskin",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "STOP Suicide Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:43Z",
    "updateDateIncludingText": "2026-05-20T08:08:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:00:45Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NE"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "IA"
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
      "sponsorshipDate": "2026-05-19",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8124ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8124\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Raskin (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to establish a grant program to support models for providing stabilization services to individuals with serious thoughts of suicide, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stabilization to Prevent Suicide Act or the STOP Suicide Act .\n#### 2. Grants to implement models for providing stabilization services\nTitle V of the Public Health Service Act is amended by inserting after section 520N ( 42 U.S.C. 290bb\u201345 ) the following:\n520O. Grants to implement models for providing stabilization services (a) In general The Assistant Secretary shall award grants, on a competitive basis, to eligible entities to implement models for providing stabilization services to individuals with serious thoughts of suicide. (b) Applications (1) In general To be eligible to receive a grant under this section, an eligible entity shall submit to the Assistant Secretary an application at such time, in such manner, and containing such information as the Assistant Secretary determines is appropriate, which shall include the plan described in paragraph (2). (2) Continuity plan An application described in paragraph (1) shall include a plan for how an eligible entity will continue to finance the provision of stabilization services supported by a grant awarded under this section following the end of the grant period of such grant. (c) Eligible uses A grant awarded under this section\u2014 (1) shall be used to provide or support the provision of stabilization services that are\u2014 (A) suicide-specific; (B) evidence-based or evidence-informed; and (C) provided in the least-restrictive setting that is appropriate for the needs of the individual to whom such services are provided; and (2) may be used to provide or support the provision of stabilization services that take the form of outpatient care, virtual care, or other technology-related innovations, which may include peer support services. (d) Grant period The term of a grant awarded under this section shall not exceed 5 years. Such term is not renewable. (e) Evaluations, training, and technical assistance The Assistant Secretary shall\u2014 (1) conduct an evaluation of the activities supported by the grants awarded under this section and disseminate, as appropriate, the findings of such evaluation; (2) provide training and other information, as appropriate, to any eligible entity that is awarded a grant under this section; and (3) provide technical assistance, as appropriate, to any eligible entity that is awarded a grant under this section. (f) Definitions In this section: (1) Eligible entity The term eligible entity means\u2014 (A) a community-based primary care or behavioral health care provider, including\u2014 (i) a school-based health center; (ii) a campus-based health center at an institution of higher education (as defined in section 101 of the Higher Education Act of 1965); (iii) a community health center; (iv) a rural health clinic (as defined in section 1861(aa) of the Social Security Act); (v) a Federally qualified health center (as defined in such section 1861(aa)); (vi) a certified community behavioral health clinic; and (vii) a children\u2019s hospital; (B) a crisis center; (C) a public health agency, including\u2014 (i) a State mental health agency; and (ii) a State health agency with mental or behavioral health functions; (D) a territory of the United States; and (E) an Indian tribe or tribal organization (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act). (2) Stabilization services The term stabilization services means a clinical intervention or treatment that\u2014 (A) reduces or eliminates a state of acute emotional crisis; (B) reduces or eliminates clear and imminent suicide risk of the patient; or (C) helps the patient establish behavioral control over acute impulsive states. (g) Authorization of appropriations There is authorized to be appropriated to carry out this section $30,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2026-03-26",
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
        "name": "Health",
        "updateDate": "2026-04-14T19:16:24Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8124ih.xml"
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
      "title": "STOP Suicide Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STOP Suicide Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stabilization to Prevent Suicide Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to establish a grant program to support models for providing stabilization services to individuals with serious thoughts of suicide, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:21Z"
    }
  ]
}
```
