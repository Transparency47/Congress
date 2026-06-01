# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1878?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1878
- Title: ATTAIN Mental Health Act
- Congress: 119
- Bill type: S
- Bill number: 1878
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-04-14T11:03:26Z
- Update date including text: 2026-04-14T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1878",
    "number": "1878",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "ATTAIN Mental Health Act",
    "type": "S",
    "updateDate": "2026-04-14T11:03:26Z",
    "updateDateIncludingText": "2026-04-14T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
            "date": "2025-05-22T17:21:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-22T17:21:30Z",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MN"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "GA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NV"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1878is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1878\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mrs. Fischer (for herself and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish an interactive online dashboard to improve public access to information about grant funding related to mental health and substance use disorder programs.\n#### 1. Short title\nThis Act may be cited as the Achieving Thorough Transparency and Accessibility for Information Navigation on Mental Health Act of 2025 or the ATTAIN Mental Health Act .\n#### 2. Interactive dashboard\n##### (a) Establishment\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this section as the Secretary ) shall establish and operate an interactive, internet website-based dashboard (referred to in this section as the dashboard ) that improves public access to information about Federal grants related to mental health and substance use disorder, including for potential applicants for such grants.\n**(2) Design**\nThe dashboard shall be designed in a manner that complies with the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n**(3) Consultation**\n**(A) In general**\nIn establishing the dashboard under paragraph (1), the Secretary may consult with\u2014\n**(i)**\nthe Director of the National Institutes of Health, the Assistant Secretary for Mental Health and Substance Use, the Director of the Indian Health Service, the Administrator of the Health Resources and Services Administration, the Secretary of Education, the Attorney General, the Secretary of Housing and Urban Development, the Secretary of Labor, the Secretary of Veterans Affairs, the Secretary of Defense, the Secretary of Homeland Security, and heads of other relevant agencies, as the Secretary determines appropriate;\n**(ii)**\nIndian Tribes and Tribal organizations (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); and\n**(iii)**\nrelevant entities who may use the dashboard, including\u2014\n**(I)**\nelementary or secondary schools; institutions of higher education, including historically Black colleges and universities (as defined for purposes of section 322 of the Higher Education Act of 1965 ( 20 U.S.C. 1061 ), Tribal colleges or universities (as defined in section 316(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1059c(b) )), and other minority-serving institutions, as such institutions are described in section 371(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1067q ); local educational agencies (as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )); State educational agencies (as defined in such section 8101); nonprofit organizations; faith or community-based organizations; clinical researchers; mental health and substance use disorder care providers; mental health and substance use disorder prevention, treatment, and recovery programs and facilities; housing services; municipal governments; law enforcement agencies; first responders; drug courts; mental health courts; veterans treatment courts; health programs administered directly by the Indian Health Service; Tribal health programs; Urban Indian organizations (as defined in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 )); and Native Hawaiian organizations (as defined in section 12(5) of the Native Hawaiian Health Care Improvement Act ( 42 U.S.C. 11711(5) )); and\n**(II)**\nany other entities that the Secretary determines are relevant.\n**(B) Topics**\nThe consultation with stakeholders and entities described in subparagraph (A)(iii) shall be with respect to elements of the dashboard, such as search functions, grant data, user-friendly design, and any other elements that the Secretary determines are appropriate for purposes of this subsection.\n**(4) Implementation plan**\nThe Secretary, in consultation with representatives of relevant agencies described in paragraph (3)(A), shall, not later than 180 days after the date of enactment of this Act, publicly issue a plan to launch the dashboard, including opportunities to improve upon existing publicly accessible websites that may be updated by the Secretary to meet the requirements under subsection (c).\n##### (b) Updates\nThe Secretary shall continually maintain the dashboard established under subsection (a) to keep all relevant, current grant opportunities posted.\n##### (c) Requirements\nThe dashboard established under subsection (a) shall, at a minimum, meet the following requirements:\n**(1)**\nProvide the following information:\n**(A)**\nThe name of each Federal grant program and, if different, the name of each associated State grant program, as available, that is designated for, or which allows an expenditure for, activities for the purposes of mental health or substance use disorder prevention, treatment, recovery, or support.\n**(B)**\nWith respect to the current fiscal year, for each program for which subgrants are not available, indicate whether applications for the Federal grant application period is open, closed, or awarded, and the opening, closing, and award dates.\n**(C)**\nFor each program for which amounts have been awarded to States for the current fiscal year with respect to a block grant described in subsection (d)(2), include, as available, whether the relevant application period for a subgrant remains open, has closed, or been awarded at the State level, and whether there will be a new subgrant competition during the current fiscal year, if such information is available from the applicable State in a manner that allows for integration of such information into the dashboard or for links to such information within the dashboard.\n**(2)**\nFor purposes of assisting applicants in identifying programs included in the dashboard, include the following information with respect to each program listed:\n**(A)**\nAny associated authorization, report, appropriation, agency program, grant number, or other information that the Secretary determines to be useful in identifying the program.\n**(B)**\nAny subgrant name used by a State, if different than the associated Federal program, if known by the Secretary.\n**(3)**\nAllow potential grant applicants to search the dashboard by key categories and location, if applicable, for which grants are available.\n**(4)**\nProvide, as appropriate, access or links to the respective program information pages and online applications.\n##### (d) Acceptance and integration of State provided data\n**(1) In general**\nThe Secretary may determine how to accept and integrate into the dashboard information voluntarily submitted by States that is relevant to the purposes of such dashboard, as described subsection (a)(1).\n**(2) Block grants**\nIn the case of mental health and substance use disorder resources made available through Federal block grants to States and Indian Tribes and Tribal organizations (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )), or Federal funding for which a specific recipient is not identified prior to its distribution to a State or Indian Tribe or Tribal organization, the Secretary may establish a method for States and Indian Tribes and Tribal organizations to voluntarily identify how Federal grants will be or were distributed, including grant names and internet website links, if different.",
      "versionDate": "2025-05-22",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-06-13T12:44:33Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1878is.xml"
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
      "title": "ATTAIN Mental Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ATTAIN Mental Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Achieving Thorough Transparency and Accessibility for Information Navigation on Mental Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an interactive online dashboard to improve public access to information about grant funding related to mental health and substance use disorder programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:32Z"
    }
  ]
}
```
