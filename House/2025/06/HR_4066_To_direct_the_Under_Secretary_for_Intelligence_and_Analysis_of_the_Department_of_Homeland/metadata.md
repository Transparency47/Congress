# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4066?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4066
- Title: Countering White Supremacist Extremism Act
- Congress: 119
- Bill type: HR
- Bill number: 4066
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2026-05-16T08:07:05Z
- Update date including text: 2026-05-16T08:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-06-23 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2025-06-20: Introduced in House

## Actions

- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-06-23 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4066",
    "number": "4066",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Countering White Supremacist Extremism Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:05Z",
    "updateDateIncludingText": "2026-05-16T08:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-23T20:27:09Z",
              "name": "Referred to"
            }
          },
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "systemCode": "hshm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4066ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4066\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Ms. Williams of Georgia introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo direct the Under Secretary for Intelligence and Analysis of the Department of Homeland Security to develop and disseminate a threat assessment regarding threats to the United States associated with foreign violent white supremacist extremist organizations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Countering White Supremacist Extremism Act .\n#### 2. Threat assessment\n##### (a) In general\nThe Under Secretary for Intelligence and Analysis of the Department of Homeland Security shall, in coordination with appropriate Federal partners, develop a terrorism threat assessment and reference aid regarding threats to the United States associated with foreign violent white supremacist extremist organizations. Consistent with the protection of classified and confidential unclassified information, the Under Secretary shall share the threat assessment developed under this section with State, local, and Tribal law enforcement officials, including officials who operate within State, local, and regional fusion centers through the Department of Homeland Security State, Local, and Regional Fusion Center Initiative established in accordance with section 210A of the Homeland Security Act of 2002 ( 6 U.S.C. 124h ).\n##### (b) Foundation, incorporation, and coordination\nThe threat assessment and reference aid developed pursuant to subsection (a)\u2014\n**(1)**\nshall be\u2014\n**(A)**\nbased on and incorporate appropriate elements of the Department of State Strategy for Countering White Identity Terrorism Globally required under section 1299F of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 22 U.S.C. 2656j ); and\n**(B)**\ndeveloped in coordination with the Office of Civil Rights and Civil Liberties of the Department of Homeland Security and other appropriate Federal agencies; and\n**(2)**\nmay be informed by existing products developed by such Office and agencies, as appropriate.\n##### (c) Overview\nThe threat assessment and reference aid shall include an overview of symbols, flags, or other references utilized by adherents of foreign violent white supremacist extremist organizations.\n##### (d) Distribution\nConsistent with the protection of classified and confidential unclassified information, the Under Secretary for Intelligence and Analysis of the Department of Homeland Security shall share the threat assessment and reference aid with the following:\n**(1)**\nState, local, and Tribal law enforcement officials, including officials who operate within State, local, and regional fusion centers through the Department of Homeland Security State, Local, and Regional Fusion Center Initiative established in accordance with section 210A of the Homeland Security Act of 2002 ( 6 U.S.C. 124h ).\n**(2)**\nAppropriate owners and operators of online platforms to assist in identifying content that may be associated with a foreign violent white supremacist extremist organization that may violate the terms of service of such online platforms, upon request from such online platforms and in consultation with the Office of Civil Rights and Civil Liberties of the Department.\n##### (e) Definitions\nIn this section:\n**(1) Foreign violent white supremacist extremist organization**\nThe term foreign violent white supremacist extremist organization means an organization based outside the United States that seeks, wholly or in part, through unlawful acts of force or violence, to support a belief in the intellectual and moral superiority of the white race over other races.\n**(2) Online platform**\nThe term online platform means internet-based information services consisting of the storage and processing of information by and at the request of a content provider and the dissemination of such content to third parties.\n##### (f) Limitation\nThe Under Secretary for Intelligence and Analysis of the Department of Homeland Security shall ensure that the threat assessment and reference aid does not contain the name or other identifiable information of any individual or organization engaged in lawful political or public discourse in the United States protected under the United States Constitution.",
      "versionDate": "2025-06-20",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-29T21:08:57Z"
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
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4066ih.xml"
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
      "title": "Countering White Supremacist Extremism Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Countering White Supremacist Extremism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Under Secretary for Intelligence and Analysis of the Department of Homeland Security to develop and disseminate a threat assessment regarding threats to the United States associated with foreign violent white supremacist extremist organizations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:31Z"
    }
  ]
}
```
