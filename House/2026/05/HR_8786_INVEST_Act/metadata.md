# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8786?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8786
- Title: INVEST Act
- Congress: 119
- Bill type: HR
- Bill number: 8786
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-27T08:53:39Z
- Update date including text: 2026-05-27T08:53:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8786",
    "number": "8786",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001067",
        "district": "9",
        "firstName": "Yvette",
        "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
        "lastName": "Clarke",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "INVEST Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:53:39Z",
    "updateDateIncludingText": "2026-05-27T08:53:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "DC"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8786ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8786\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Ms. Clarke of New York (for herself, Ms. Norton , Ms. Kamlager-Dove , and Ms. Crockett ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide the work opportunity tax credit with respect to the hiring of veterans in the field of renewable energy.\n#### 1. Short title\nThis Act may be cited as the Incentives for our Nation\u2019s Veterans in Energy Sustainability Technologies Act or as the INVEST Act .\n#### 2. Work opportunity tax credit for veterans hired in the field of renewable energy\n##### (a) In general\nSection 51(d)(14) of the Internal Revenue Code of 1986 is amended to read as follows:\n(14) Certain veterans hired in the field of renewable energy (A) In general For purposes of this subpart, an individual shall be treated as a member of a targeted group if such individual is a specified veteran, but qualified wages with respect to such individual shall include only wages attributable to services rendered in a field of renewable energy. (B) Specified veteran For purposes of this paragraph, the term specified veteran means any veteran (as defined in paragraph (3)) who is certified by the designated local agency as\u2014 (i) having received a credential or certification from the Department of Defense of military occupational specialty or skill in a field of renewable energy or with respect to advanced manufacturing, machinist or welding, or engineering, (ii) having completed a vocational degree in a field of renewable energy during the 1-year period ending on the hiring date, or (iii) having completed a LEED certification with the United States Green Building Council. (C) Renewable energy For purposes of this paragraph, renewable energy means resources that rely on fuel sources that restore themselves over short periods of time and do not diminish, including the Sun, wind, moving water, organic plant and waste material, and the Earth\u2019s heat. .\n##### (b) Treatment of possessions\n**(1) Payments to possessions**\n**(A) Mirror code possessions**\nThe Secretary of the Treasury shall pay to each possession of the United States with a mirror code tax system amounts equal to the loss to that possession by reason of the amendment made by this section. Such amounts shall be determined by the Secretary of the Treasury based on information provided by the government of the respective possession of the United States.\n**(B) Other possessions**\nThe Secretary of the Treasury shall pay to each possession of the United States which does not have a mirror code tax system the amount estimated by the Secretary of the Treasury as being equal to the loss to that possession that would have occurred by reason of the amendment made by this section if a mirror code tax system had been in effect in such possession. The preceding sentence shall not apply with respect to any possession of the United States unless such possession establishes to the satisfaction of the Secretary that the possession has implemented (or, at the discretion of the Secretary, will implement) an income tax benefit which is substantially equivalent to the income tax credit in effect after the amendments made by this section.\n**(2) Coordination with credit allowed against united states income taxes**\nThe credit allowed against United States income taxes for any taxable year under the amendment made by this section to section 51 of the Internal Revenue Code of 1986 to any person with respect to any qualified veteran shall be reduced by the amount of any credit (or other tax benefit described in paragraph (1)(B)) allowed to such person against income taxes imposed by the possession of the United States by reason of this subsection with respect to such qualified veteran for such taxable year.\n**(3) Definitions and special rules**\n**(A) Possession of the united states**\nFor purposes of this subsection, the term possession of the United States includes American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, the Commonwealth of Puerto Rico, and the United States Virgin Islands.\n**(B) Mirror code tax system**\nFor purposes of this subsection, the term mirror code tax system means, with respect to any possession of the United States, the income tax system of such possession if the income tax liability of the residents of such possession under such system is determined by reference to the income tax laws of the United States as if such possession were the United States.\n**(C) Treatment of payments**\nFor purposes of section 1324(b)(2) of title 31, United States Code, the payments under this subsection shall be treated in the same manner as a refund due from credit provisions described in such section.\n##### (c) Effective date\nThe amendment made by this section shall apply to individuals who begin work for the employer after December 31, 2025.",
      "versionDate": "2026-05-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8786ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "INVEST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T08:53:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Incentives for our Nation\u2019s Veterans in Energy Sustainability Technologies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T08:53:39Z"
    },
    {
      "title": "INVEST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:53:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide the work opportunity tax credit with respect to the hiring of veterans in the field of renewable energy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:48:34Z"
    }
  ]
}
```
