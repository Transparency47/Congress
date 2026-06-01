# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5417
- Title: Health Access Innovation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5417
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-12-05T22:48:30Z
- Update date including text: 2025-12-05T22:48:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5417",
    "number": "5417",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Health Access Innovation Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:48:30Z",
    "updateDateIncludingText": "2025-12-05T22:48:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:04:35Z",
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
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5417ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5417\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Ms. Williams of Georgia (for herself, Ms. Clarke of New York , and Mr. Kennedy of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize the Secretary of Health and Human Services to award grants to faith-or community-based organizations to address persistent health inequities and chronic disease challenges.\n#### 1. Short title\nThis Act may be cited as the Health Access Innovation Act of 2025 .\n#### 2. Health Equity Innovation Grant Program\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. Health Equity Innovation Grant Program (a) In general The Secretary may award grants to eligible entities to expand access to culturally and linguistically appropriate care, encourage innovation, and address persistent health inequities and chronic disease challenges, including by\u2014 (1) paying the costs of necessary medical services, health screenings, tests, and other preventive services; (2) expanding access to care, such as by\u2014 (A) expanding access to health care and public health services; (B) expanding the diversity of types of health workers; (C) expanding the availability of culturally and linguistically appropriate services; and (D) addressing other social determinants of health and barriers to receiving timely and quality care; (3) supporting\u2014 (A) community health navigators; (B) community health workers (also known as promotores de salud ); (C) peer support specialists; (D) community health representatives; and (E) other health care professionals, including those who work with faith-or community-based organizations as trusted messengers with lived experiences to support access and connection to care; (4) expanding the capacity of the eligible entity; and (5) carrying out other programs that address social determinants of health. (b) Eligible entities To be eligible for a grant under this section, an entity shall be a faith-or community-based organization that\u2014 (1) has demonstrated an ability to address chronic health disparities and health conditions in communities disproportionately affected by such disparities and conditions; and (2) is located in a medically underserved community or a designated health professional shortage area. (c) Priority In awarding grants under this section, the Secretary shall give priority to eligible entities that established or operated one or more health workforce or health care access programs during a public health emergency. (d) Community-Based organization defined In this section, the term community-based organization has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965. (e) Authorization of appropriations (1) In general There is authorized to be appropriated to carry out this section\u2014 (A) $50,000,000 for fiscal year 2026; (B) $55,000,000 for fiscal year 2027; (C) $60,000,000 for fiscal year 2028; (D) $65,000,000 for fiscal year 2029; and (E) $70,000,000 for fiscal year 2029. (2) Administrative costs Of the funds appropriated to carry out this section, not more than 5 percent may be used by the Secretary for the administrative costs of carrying out this section. .",
      "versionDate": "2025-09-16",
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
        "actionDate": "2025-09-16",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2825",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Health Access Innovation Act of 2025",
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
        "updateDate": "2025-09-29T13:21:44Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5417ih.xml"
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
      "title": "Health Access Innovation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Health Access Innovation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize the Secretary of Health and Human Services to award grants to faith- or community-based organizations to address persistent health inequities and chronic disease challenges.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T05:33:23Z"
    }
  ]
}
```
