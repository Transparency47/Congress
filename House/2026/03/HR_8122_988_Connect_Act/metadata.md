# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8122?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8122
- Title: 9–8–8 Connect Act
- Congress: 119
- Bill type: HR
- Bill number: 8122
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-14T19:49:47Z
- Update date including text: 2026-04-14T19:49:47Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8122",
    "number": "8122",
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
    "title": "9\u20138\u20138 Connect Act",
    "type": "HR",
    "updateDate": "2026-04-14T19:49:47Z",
    "updateDateIncludingText": "2026-04-14T19:49:47Z"
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
          "date": "2026-03-26T14:00:05Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8122ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8122\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Raskin (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to award grants to eligible crisis centers to provide follow-up services to individuals receiving suicide prevention and crisis intervention services, to amend the Communications Act of 1934 to improve the accessibility of 9\u20138\u20138, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 9\u20138\u20138 Connect Act .\n#### 2. Grants for follow-up services to individuals receiving suicide prevention and crisis intervention services\nTitle V of the Public Health Service Act is amended by inserting after section 520E\u20134 ( 42 U.S.C. 290bb\u201336d ) the following:\n520E\u20135. Follow-up services to individuals receiving suicide prevention and crisis intervention services (a) In general The Secretary, acting through the Assistant Secretary, shall award grants to eligible crisis centers to provide follow-up services to individuals receiving suicide prevention and crisis intervention services. (b) Eligibility To be eligible to seek a grant under this section, a crisis center shall be a member of the network of crisis centers coordinated under section 520E\u20133(b)(1). (c) Selection The Secretary shall select recipients of grants under this section based on the relative needs, including capacity and service gaps, of the eligible crisis centers applying for such grants. (d) Technical assistance The Secretary shall provide technical assistance to recipients of grants under this section regarding best practices for the implementation of services through such grants. (e) Use of funds (1) In general A crisis center receiving a grant under this section shall use the grant to provide follow-up services to individuals receiving suicide prevention and crisis intervention services such as\u2014 (A) individuals who were callers at risk of, or on behalf of someone at risk of, suicide or a mental health or suicidal crisis; and (B) to the extent possible, individuals who\u2014 (i) received a response from a mobile crisis team; or (ii) made a visit to an urgent behavioral health clinic, a crisis receiving and stabilization facility, an emergency department, an inpatient unit, or another short-term crisis care site. (2) Follow-up services Follow-up services referred to in paragraph (1) may include\u2014 (A) check-ins to assess well-being and level of risk; (B) outreach to ensure engagement in services and supports, in coordination with mobile crisis service providers if involved; (C) collaboration with family, caregivers, and natural social supports; and (D) referrals based on the needed level of care. (f) Authorization of appropriations To carry out this section, there is authorized to be appropriated $30,000,000 for fiscal year 2027, to remain available until expended. .\n#### 3. 9\u20138\u20138 Improvement\n##### (a) Definitions\nIn this section:\n**(1) 9\u20138\u20138**\nThe term 9\u20138\u20138 means 9\u20138\u20138, as designated as the universal telephone number within the United States for the purpose of the national suicide prevention and mental health crisis hotline system under section 251(e)(4) of the Communications Act of 1934 ( 47 U.S.C. 251(e)(4) ).\n**(2) Commercial mobile service**\nThe term commercial mobile service has the meaning given the term in section 332(d) of the Communications Act of 1934 ( 47 U.S.C. 332(d) ).\n**(3) Non-service-initialized handset**\nThe term non-service-initialized handset has the meaning given the term in section 9.10(o)(3)(i) of title 47, Code of Federal Regulations, or any successor regulation.\n##### (b) Transmission of all calls and texts\n**(1) In general**\nNot later than 270 days after the date of enactment of this Act, the Federal Communications Commission shall promulgate regulations to ensure that each provider of commercial mobile service transmits all calls and text messages made or sent to 9\u20138\u20138, including a call or text message that originates from a non-service-initialized handset (if the call or text message originates on a phone using a compliant radio frequency protocol of the provider).\n**(2) Implementation**\nA provider of commercial mobile service shall comply with the regulations promulgated under paragraph (1) not later than 1 year after the date on which the regulations are promulgated.\n##### (c) Configuration of multi-Line telephone systems for direct dialing\n**(1) In general**\nSection 721 of the Communications Act of 1934 ( 47 U.S.C. 623 ) is amended\u2014\n**(A)**\nin the section heading, by inserting and 9\u20138\u20138 after 9\u20131\u20131 ;\n**(B)**\nin subsection (a), by inserting or 9\u20138\u20138 after 9\u20131\u20131 ; and\n**(C)**\nin subsection (b), by inserting or 9\u20138\u20138 after 9\u20131\u20131 .\n**(2) Applicability**\n**(A) In general**\nThe amendments made by paragraph (1) shall apply to actions occurring on and after the date that is 2 years after the date of enactment of this Act.\n**(B) Exception**\nThe amendment made by paragraph (1)(C) shall not apply to the management or operation of a multi-line telephone system installed before the date that is 2 years after the date of enactment of this Act, if the system is not able to be configured to satisfy the requirements of the amendment, without an improvement to the hardware or software of the system.",
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
        "updateDate": "2026-04-14T19:49:47Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8122ih.xml"
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
      "title": "9\u20138\u20138 Connect Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "9\u20138\u20138 Connect Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to award grants to eligible crisis centers to provide follow-up services to individuals receiving suicide prevention and crisis intervention services, to amend the Communications Act of 1934 to improve the accessibility of 9-8-8, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:27Z"
    }
  ]
}
```
