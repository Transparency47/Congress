# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2278?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2278
- Title: Survivor Benefits Delivery Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2278
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-05-12T17:21:18Z
- Update date including text: 2025-05-12T17:21:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2278",
    "number": "2278",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000472",
        "district": "39",
        "firstName": "Mark",
        "fullName": "Rep. Takano, Mark [D-CA-39]",
        "lastName": "Takano",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Survivor Benefits Delivery Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-12T17:21:18Z",
    "updateDateIncludingText": "2025-05-12T17:21:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T18:09:23Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2278ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2278\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Takano introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to improve equitable access to certain benefits under the laws administered by the Secretary of Veterans Affairs and to improve certain outreach to individuals who served uniformed services and dependents of such individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Survivor Benefits Delivery Improvement Act of 2025 .\n#### 2. Equitable access to certain benefits of Department of Veterans Affairs for survivors of veterans\n##### (a) Short title\nThis section may be cited as the Survivor Benefits Data Collection Act of 2025 .\n##### (b) Collection of demographic data\n**(1) Collection**\nChapter 53 of title 38, United States Code, is amended by adding at the end the following new section (and conforming the table of sections at the beginning of such chapter accordingly):\n5322. Demographic data of certain beneficiaries (a) Collection The Secretary, in consultation with the entities described in subsection (b), shall\u2014 (1) develop a method to collect the demographic data of\u2014 (A) each covered survivor receiving disability and indemnity compensation under chapter 13 of this title, pension under chapter 15 of this title, or increased pension (or additional compensation or allowances) under this title based on the need of regular aid and attendance or by reason of being permanently housebound; and (B) each person who receives burial benefits under chapter 23 of this title; and (2) collect demographic data pursuant to the method developed under paragraph (1). (b) Entities for consultation The entities described in this subsection are the following: (1) The Advisory Committee on Minority Veterans established under section 544 of this title. (2) The Advisory Committee on Women Veterans established under section 542 of this title. (3) The Veterans\u2019 Family, Caregiver, and Survivor Advisory Committee of the Department of Veterans Affairs, or successor advisory committee. (4) Veterans service organizations. (c) Designation of underserved demographics The Secretary shall\u2014 (1) designate as an underserved demographic any demographic the Secretary determines, taking into account the demographic data collected under subsection (a), is underserved with respect to the benefits specified in such subsection; and (2) review such designations on at least a biennial basis and update as appropriate. (d) Inclusion in annual reports For each annual benefits report of the Veterans Benefits Administration, the Secretary shall include as part of the report information concerning the demographic data collected under subsection (a) during the fiscal year covered by the report. (e) Effect on application Nothing in this section shall be construed as requiring any person to submit demographic data or as authorizing the Secretary to consider whether a person submits demographic data in evaluating any claim for benefits under the laws administered by the Secretary. (f) Definitions In this section: (1) The term covered survivor means a surviving spouse, child, or parent of a veteran. (2) The term demographic data includes, with respect to an individual, the following: (A) Race. (B) Ethnicity. (C) Tribal affiliation, if any. (D) LGBTQIA+ status. (E) Geographic location. (3) The term veterans service organization means any organization recognized by the Secretary under section 5902 of this title. .\n**(2) Deadlines; applicability**\n**(A) Deadline for collection**\nThe Secretary of Veterans Affairs shall develop the data collection method under subsection (a) of section 5322 of title 38, United States Code (as added by paragraph (1)), and commence the collection of data pursuant to such method, by not later than 180 days after the date of the enactment of this Act.\n**(B) Deadline for initial designations**\nThe Secretary shall make the initial designation of any underserved demographics under subsection (c) of such section 5322 by not later than one year after the date on which the Secretary commences the collection of data under subsection (a) of such section.\n**(C) Applicability regarding annual reports**\nThe requirement under subsection (d) of such section 5322 shall apply with respect to annual benefits reports of the Veterans Benefits Administration submitted on or after the date that is one year after the date on which the Secretary commences the collection of data under subsection (a) of such section.\n##### (c) Outreach and education\n**(1) Strategy for underserved demographics**\nNot later than one year after the date of initial designation, the Secretary shall develop and submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives an outreach and education strategy for raising awareness regarding the benefits specified in section 5322(a) of title 38, United States Code (as added by subsection (b)), among covered survivors who belong to an underserved demographic.\n**(2) Eligibility of veterans for certain burial benefits**\n**(A) Outreach plan**\nNot later than 180 days after the date of initial designation, the Under Secretary for Memorial Affairs shall develop and submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate an outreach strategy for raising awareness regarding eligibility for burial in a national cemetery under section 2303 of title 38, United States Code, among veterans and beneficiaries who belong to an underserved demographic.\n**(B) Education activities**\nThe Under Secretary shall carry out education activities pursuant to the plan developed under subparagraph (A) to ensure that the veterans and beneficiaries specified in such paragraph are made aware of any eligibility specified in such subparagraph.\n**(C) Reports**\nNot later than one year after the date of initial designation, and annually thereafter for five years, the Under Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report on the efforts taken by the Under Secretary pursuant to this paragraph.\n**(3) Definitions**\nIn this subsection:\n**(A)**\nThe term covered survivor has the meanings given that term in section 5322(e) of title 38, United States Code (as added by subsection (b)).\n**(B)**\nThe term date of initial designation means the date on which the Secretary makes the initial designation of any underserved demographics.\n**(C)**\nThe term underserved demographic means a demographic designated as an underserved demographic by the Secretary of Veterans Affairs under section 5322(c) of title 38, United States Code (as added by subsection (b)).\n##### (d) Assessment and strategy for Office of Survivors Assistance\nNot later than one year after the date of the enactment of this Act, the Secretary shall\u2014\n**(1)**\nconduct an assessment of the resources of the Office of Survivors Assistance of the Department of Veterans Affairs, or any successor office; and\n**(2)**\ndevelop a strategy to ensure the availability of resources necessary for the function of such office, as determined by the Secretary as a result of the assessment.\n#### 3. Improvements to outreach services provided by Secretary of Veterans Affairs to individuals who served in the uniformed services and dependents of such individuals\n##### (a) Short title\nThis section may be cited as the Survivor Solid Start Act of 2025 .\n##### (b) Expansion of outreach services\nSubchapter I of chapter 63 of title 38, United States Code, is amended\u2014\n**(1)**\nin section 6301(b)\u2014\n**(A)**\nby redesignating paragraphs (1) through (3) as paragraphs (2) through (4), respectively;\n**(B)**\nby inserting before paragraph (2) (as so redesignated) the following new paragraph:\n(1) the term covered individual means\u2014 (A) a veteran; or (B) an individual who served in the uniformed services (as defined in section 1965(6) of this title); ;\n**(C)**\nin paragraph (2) (as so redesignated), by striking veterans each place it appears and inserting covered individuals ; and\n**(D)**\nin paragraph (4) (as so redesignated), by striking a person who served in the active military, naval, air, or space service and inserting a covered individual ;\n**(2)**\nin section 6302(b), by striking eligible veterans each place it appears and inserting covered individuals ;\n**(3)**\nin section 6303\u2014\n**(A)**\nin subsection (a), by striking eligible veterans and inserting covered individuals ;\n**(B)**\nin subsection (c)(1)(A), by striking eligible veterans and inserting covered individuals ;\n**(C)**\nin subsection (c)(2), by striking veteran or dependent each place it appears and inserting covered individual or eligible dependent ; and\n**(D)**\nin subsection (d), by striking veterans and inserting covered individuals ;\n**(4)**\nin section 6306\u2014\n**(A)**\nin subsection (a), by striking eligible veteran and inserting covered individual ; and\n**(B)**\nin subsection (b)\u2014\n**(i)**\nby striking opportunities for veterans and inserting opportunities for covered individuals ; and\n**(ii)**\nby striking eligible veterans and inserting covered individuals ; and\n**(5)**\nin section 6308, by adding at the end the following new subsection:\n(c) Outreach services for surviving eligible dependents (1) (A) Upon receipt of notification of the death of a covered individual, the Secretary, acting through the Under Secretary for Benefits, shall provide outreach services, by mail, email, and telephone, to each eligible dependent of such individual not less than once each quarter calendar year until the eligible dependent files a claim for a benefit under laws administered by the Secretary. (B) In the case of an eligible dependent described in subparagraph (A) who is a minor child, the Secretary shall provide such outreach services to the legal guardian of the eligible dependent. (C) If the Secretary does not have the contact information of an eligible dependent or legal guardian described in subparagraph (A) or (B), the Secretary shall make reasonable efforts to obtain such contact information to carry out this subsection. (D) An eligible dependent or legal guardian described in subparagraph (A) or (B) may elect to not receive, or to receive fewer, outreach services under this subsection. Not less than once each calendar year, the Secretary shall notify each such eligible dependent or legal guardian of the option to make such an election. (2) Outreach services under this subsection shall provide an eligible dependent with information including the following: (A) Contact information for the Office of Survivors Assistance established under section 321 of this title. (B) Information regarding assistance in filing a claim for a benefit under laws administered by the Secretary furnished by\u2014 (i) a veterans service organization recognized under section 5902 of this title; or (ii) an attorney, agent, or other entity recognized under section 5904 of this title. (C) How to find an entity\u2014 (i) described in clause (i) or (ii) of subparagraph (B); and (ii) located near the residence of the eligible dependent. (3) In developing and revising materials used in outreach services under this subsection, the Secretary shall consult with entities including the following: (A) Veterans service organizations recognized under section 5902 of this title. (B) The Advisory Committee on Women Veterans established under section 542 of this title. (C) The Advisory Committee on Minority Veterans established under section 544 of this title. (D) The Veterans\u2019 Family, Caregiver, and Survivor Advisory Committee of the Department, or successor advisory committee. .\n##### (c) Personnel\nThe Secretary of Veterans Affairs shall establish at least 5, but not more than 10, full-time equivalent positions at call centers of the Department of Veterans Affairs to carry out subsection (c) of section 6308 of such title, as added by subsection (b).",
      "versionDate": "2025-03-21",
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
        "updateDate": "2025-05-12T17:21:18Z"
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
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2278ih.xml"
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
      "title": "Survivor Benefits Delivery Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T12:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Survivor Benefits Delivery Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T12:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Survivor Solid Start Act of 2025",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-04-02T12:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to improve equitable access to certain benefits under the laws administered by the Secretary of Veterans Affairs and to improve certain outreach to individuals who served uniformed services and dependents of such individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T12:03:24Z"
    }
  ]
}
```
