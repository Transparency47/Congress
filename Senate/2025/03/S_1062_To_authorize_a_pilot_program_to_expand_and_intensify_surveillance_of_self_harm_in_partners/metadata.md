# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1062?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1062
- Title: Suicide Prevention Act
- Congress: 119
- Bill type: S
- Bill number: 1062
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S1747)
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S1747)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1062",
    "number": "1062",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Suicide Prevention Act",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S1747)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
        "item": {
          "date": "2025-03-13T22:32:39Z",
          "name": "Referred To"
        }
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1062is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1062\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Reed (for himself and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo authorize a pilot program to expand and intensify surveillance of self-harm in partnership with State and local public health departments, to establish a grant program to provide self-harm and suicide prevention services in hospital emergency departments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Suicide Prevention Act .\n#### 2. Syndromic surveillance of self-harm behaviors program\nTitle III of the Public Health Service Act is amended by inserting after section 317V of such Act ( 42 U.S.C. 247b\u201324 ) the following:\n317W. Syndromic surveillance of self-harm behaviors program (a) In general The Secretary shall award grants to State, local, Tribal, and territorial public health departments for the expansion of surveillance of self-harm. (b) Data sharing by grantees As a condition of receipt of such grant under subsection (a), each grantee shall agree to share with the Centers for Disease Control and Prevention in real time, to the extent feasible and as specified in the grant agreement, data on suicides and self-harm for purposes of\u2014 (1) tracking and monitoring self-harm to inform response activities to suicide clusters; (2) informing prevention programming for identified at-risk populations; and (3) conducting or supporting research. (c) Disaggregation of data The Secretary shall provide for the data collected through surveillance of self-harm under subsection (b) to be disaggregated by the following categories: (1) Nonfatal self-harm data of any intent. (2) Data on suicidal ideation. (3) Data on self-harm where there is no evidence, whether implicit or explicit, of suicidal intent. (4) Data on self-harm where there is evidence, whether implicit or explicit, of suicidal intent. (5) Data on self-harm where suicidal intent is unclear based on the available evidence. (d) Priority In making awards under subsection (a), the Secretary shall give priority to eligible entities that are\u2014 (1) located in a State with an age-adjusted rate of nonfatal suicidal behavior that is above the national rate of nonfatal suicidal behavior, as determined by the Director of the Centers for Disease Control and Prevention; (2) serving an Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act) with an age-adjusted rate of nonfatal suicidal behavior that is above the national rate of nonfatal suicidal behavior, as determined through appropriate mechanisms determined by the Secretary in consultation with Indian Tribes; or (3) located in a State with a high rate of coverage of statewide (or Tribal) emergency department visits, as determined by the Director of the Centers for Disease Control and Prevention. (e) Geographic distribution In making grants under this section, the Secretary shall make an effort to ensure geographic distribution, taking into account the unique needs of rural communities, including\u2014 (1) communities with an incidence of individuals with serious mental illness, demonstrated suicidal ideation or behavior, or suicide rates that are above the national average, as determined by the Assistant Secretary for Mental Health and Substance Use; (2) communities with a shortage of prevention and treatment services, as determined by the Assistant Secretary for Mental Health and Substance Use and the Administrator of the Health Resources and Services Administration; and (3) other appropriate community-level factors and social determinants of health such as income, employment, and education. (f) Period of participation To be selected as a grant recipient under this section, a State, local, Tribal, or territorial public health department shall agree to participate in the program for a period of not less than 4 years. (g) Technical assistance The Secretary shall provide technical assistance and training to grantees for collecting and sharing the data under subsection (b). (h) Data sharing by HHS Subject to subsection (c), the Secretary shall, with respect to data on self-harm that is collected pursuant to this section, share and integrate such data through\u2014 (1) the platform of the National Syndromic Surveillance Program Early Notification of Community-Based Epidemics (ESSENCE) (or any successor platform); (2) the National Violent Death Reporting System (or any successor platform), as appropriate; or (3) another appropriate surveillance program, including such a program that collects data on suicides and self-harm among special populations, such as members of the military and veterans. (i) Rule of construction regarding applicability of privacy protections Nothing in this section shall be construed to limit or alter the application of Federal or State law relating to the privacy of information to data or information that is collected or created under this section. (j) Report (1) Submission Not later than 3 years after the date of enactment of the Suicide Prevention Act , the Secretary shall evaluate the suicide and self-harm syndromic surveillance systems at the Federal, State, and local levels and submit a report to Congress on the data collected under subsection (b) in a manner that prevents the disclosure of individually identifiable information, at a minimum, consistent with all applicable privacy laws and regulations. (2) Contents In addition to the data collected under subsection (b), the report under paragraph (1) shall include\u2014 (A) challenges and gaps in data collection and reporting; (B) recommendations to address such gaps and challenges; and (C) a description of any public health responses initiated at the Federal, State, or local level in response to the data collected. (k) Authorization of appropriations To carry out this section, there are authorized to be appropriated $30,000,000 for each of fiscal years 2026 through 2030. .\n#### 3. Grants to provide self-harm and suicide prevention services\nSubpart 3 of part B of title V of the Public Health Service Act ( 42 U.S.C. 290bb\u201331 et seq. ) is amended by adding at the end the following:\n520O. Grants to provide self-harm and suicide prevention services (a) In general The Secretary shall award grants to hospital emergency departments to provide self-harm and suicide prevention services. (b) Activities supported (1) In general A hospital emergency department awarded a grant under subsection (a) shall use amounts under the grant to implement a program or protocol to better prevent suicide attempts among hospital patients after discharge, which may include\u2014 (A) screening patients for self-harm and suicide in accordance with the standards of practice described in subsection (e)(1) and standards of care established by appropriate medical and advocacy organizations; (B) providing patients short-term self-harm and suicide prevention services in accordance with the results of the screenings described in subparagraph (A); and (C) referring patients, as appropriate, to a health care facility or provider for purposes of receiving long-term self-harm and suicide prevention services, and providing any additional follow up services and care identified as appropriate as a result of the screenings and short-term self-harm and suicide prevention services described in subparagraphs (A) and (B). (2) Use of funds to hire and train staff Amounts awarded under subsection (a) may be used to hire clinical social workers, mental and behavioral health care professionals, and support staff as appropriate, and to train existing staff and newly hired staff to carry out the activities described in paragraph (1). (c) Grant terms A grant awarded under subsection (a)\u2014 (1) shall be for a period of 3 years; and (2) may be renewed subject to the requirements of this section. (d) Applications A hospital emergency department seeking a grant under subsection (a) shall submit an application to the Secretary at such time, in such manner, and accompanied by such information as the Secretary may require. (e) Standards of Practice (1) In general Not later than 180 days after the date of the enactment of this section, the Secretary shall develop standards of practice for screening patients for self-harm and suicide for purposes of carrying out subsection (b)(1)(C). (2) Consultation The Secretary shall develop the standards of practice described in paragraph (1) in consultation with individuals and entities with expertise in self-harm and suicide prevention, including public, private, and nonprofit entities. (f) Reporting (1) Reports to the Secretary (A) In general A hospital emergency department awarded a grant under subsection (a) shall, at least quarterly for the duration of the grant, submit to the Secretary a report evaluating the activities supported by the grant. (B) Matters to be included The report required under subparagraph (A) shall include\u2014 (i) the number of patients receiving\u2014 (I) screenings carried out at the hospital emergency department; (II) short-term self-harm and suicide prevention services at the hospital emergency department; and (III) referrals to health care facilities for the purposes of receiving long-term self-harm and suicide prevention; (ii) information on the adherence of the hospital emergency department to the standards of practice described in subsection (e)(1); and (iii) other information as the Secretary determines appropriate to evaluate the use of grant funds. (2) Reports to Congress Not later than 2 years after the date of the enactment of the Suicide Prevention Act , and biennially thereafter, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report on the grant program under this section, including\u2014 (A) a summary of reports received by the Secretary under paragraph (1); and (B) an evaluation of the program by the Secretary. (g) Authorization of appropriations To carry out this section, there are authorized to be appropriated $30,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-03-13",
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
        "updateDate": "2025-04-04T12:47:57Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1062is.xml"
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
      "title": "Suicide Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Suicide Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize a pilot program to expand and intensify surveillance of self-harm in partnership with State and local public health departments, to establish a grant program to provide self-harm and suicide prevention services in hospital emergency departments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:26Z"
    }
  ]
}
```
