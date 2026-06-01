# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/136?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/136
- Title: Veteran Overmedication and Suicide Prevention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 136
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-01-08T09:06:33Z
- Update date including text: 2026-01-08T09:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-03 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-03 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/136",
    "number": "136",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Veteran Overmedication and Suicide Prevention Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T09:06:33Z",
    "updateDateIncludingText": "2026-01-08T09:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:27:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-03T17:40:53Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-03",
      "state": "VA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NJ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CO"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr136ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 136\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Buchanan (for himself and Mr. Connolly ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to conduct an independent review of the deaths of certain veterans by suicide, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veteran Overmedication and Suicide Prevention Act of 2025 .\n#### 2. Department of Veterans Affairs independent review of certain deaths of veterans by suicide\n##### (a) Review required\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall seek to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine under which the National Academies shall conduct a review of the deaths of all covered veterans who died by suicide during the five-year period ending on the date of the enactment of this Act, regardless of whether information relating to such deaths has been reported by the Centers for Disease Control and Prevention.\n**(2) Elements**\nThe review required by paragraph (1) shall include the following:\n**(A)**\nThe total number of covered veterans who died by suicide during the five-year period ending on the date of the enactment of this Act.\n**(B)**\nThe total number of covered veterans who died by a violent death during such five-year period.\n**(C)**\nThe total number of covered veterans who died by an accidental death during such five-year period.\n**(D)**\nA description of each covered veteran described in subparagraphs (A) through (C), including age, gender, race, and ethnicity.\n**(E)**\nA comprehensive list of prescribed medications and legal or illegal substances as annotated on toxicology reports of covered veterans described in subparagraphs (A) through (C), specifically listing any medications that carried a black box warning, were prescribed for off-label use, were psychotropic, or carried warnings that included suicidal ideation.\n**(F)**\nA summary of medical diagnoses by physicians of the Department of Veterans Affairs or physicians providing services to covered veterans through programs of the Department that led to the prescribing of medications referred to in subparagraph (E) in cases of post-traumatic stress disorder, traumatic brain injury, military sexual trauma, and other anxiety and depressive disorders.\n**(G)**\nThe number of instances in which a covered veteran described in subparagraph (A), (B), or (C) was concurrently on multiple medications prescribed by physicians of the Department or physicians providing services to veterans through programs of the Department to treat post-traumatic stress disorder, traumatic brain injury, military sexual trauma, other anxiety and depressive disorders, or instances of comorbidity.\n**(H)**\nThe number of covered veterans described in subparagraphs (A) through (C) who were not taking any medication prescribed by a physician of the Department or a physician providing services to veterans through a program of the Department.\n**(I)**\nWith respect to the treatment of post-traumatic stress disorder, traumatic brain injury, military sexual trauma, or other anxiety and depressive disorders, the percentage of covered veterans described in subparagraphs (A) through (C) who received a non-medication first-line treatment compared to the percentage of such veterans who received medication only.\n**(J)**\nWith respect to the treatment of covered veterans described in subparagraphs (A) through (C) for post-traumatic stress disorder, traumatic brain injury, military sexual trauma, or other anxiety and depressive disorders, the number of instances in which a non-medication first-line treatment (such as cognitive behavioral therapy) was attempted and determined to be ineffective for such a veteran, which subsequently led to the prescribing of a medication referred to in subparagraph (E).\n**(K)**\nA description and example of how the Department determines and continually updates the clinical practice guidelines governing the prescribing of medications.\n**(L)**\nAn analysis of the use by the Department, including protocols or practices at medical facilities of the Department, of systematically measuring pain scores during clinical encounters under the Pain as the 5th Vital Sign Toolkit of the Department and an evaluation of the relationship between the use of such measurements and the number of veterans concurrently on multiple medications prescribed by physicians of the Department.\n**(M)**\nA description of the efforts of the Department to maintain appropriate staffing levels for mental health professionals, such as mental health counselors, marriage and family therapists, and other appropriate counselors, including\u2014\n**(i)**\na description of any impediments to carry out the education, training, and hiring of mental health counselors and marriage and family therapists under section 7302(a) of title 38, United States Code, and strategies for addressing those impediments;\n**(ii)**\na description of the objectives, goals, and timing of the Department with respect to increasing the representation of such counselors and therapists in the behavioral health workforce of the Department, including\u2014\n**(I)**\na review of eligibility criteria for such counselors and therapists and a comparison of such criteria to that of other behavioral health professions in the Department; and\n**(II)**\nan assessment of the participation of such counselors and therapists in the mental health professionals trainee program of the Department and any impediments to such participation;\n**(iii)**\nan assessment of the development by the Department of hiring guidelines for mental health counselors, marriage and family therapists, and other appropriate counselors;\n**(iv)**\na description of how the Department\u2014\n**(I)**\nidentifies gaps in the supply of mental health professionals; and\n**(II)**\ndetermines successful staffing ratios for mental health professionals of the Department;\n**(v)**\na description of actions taken by the Secretary, in consultation with the Director of the Office of Personnel Management, to create an occupational series for mental health counselors and marriage and family therapists of the Department and a timeline for the creation of such an occupational series; and\n**(vi)**\na description of actions taken by the Secretary to ensure that the national, regional, and local professional standards boards for mental health counselors and marriage and family therapists are comprised of only mental health counselors and marriage and family therapists and that the liaison from the Department to such boards is a mental health counselor or marriage and family therapist.\n**(N)**\nThe percentage of covered veterans described in subparagraphs (A) through (C) with combat experience or trauma related to combat experience (including military sexual trauma, traumatic brain injury, and post-traumatic stress).\n**(O)**\nAn identification of the medical facilities of the Department with markedly high prescription rates and suicide rates for veterans receiving treatment at those facilities.\n**(P)**\nAn analysis, by State, of programs of the Department that collaborate with State Medicaid agencies and the Centers for Medicare and Medicaid Services, including the following:\n**(i)**\nAn analysis of the sharing of prescription and behavioral health data for veterans.\n**(ii)**\nAn analysis of whether Department staff check with State prescription drug monitoring programs before prescribing medications to veterans.\n**(iii)**\nA description of the procedures of the Department for coordinating with prescribers outside of the Department to ensure that veterans are not overprescribed.\n**(iv)**\nA description of actions that the Department takes when a veteran is determined to be overprescribed.\n**(Q)**\nAn analysis of the collaboration of medical centers of the Department with medical examiners\u2019 offices or local jurisdictions to determine veteran mortality and cause of death.\n**(R)**\nAn identification and determination of a best practice model to collect and share veteran death certificate data between the Department of Veterans Affairs, the Department of Defense, States, and tribal entities.\n**(S)**\nA description of how data relating to death certificates of veterans is collected, determined, and reported by the Department of Veterans Affairs.\n**(T)**\nAn assessment of any patterns apparent to the National Academies of Sciences, Engineering, and Medicine based on the review conducted under paragraph (1).\n**(U)**\nSuch recommendations for further action that would improve the safety and well-being of veterans as the National Academies of Sciences, Engineering, and Medicine determine appropriate.\n**(3) Compilation of data**\n**(A) Form of compilation**\nThe Secretary of Veterans Affairs shall ensure that data compiled under paragraph (2) is compiled in a manner that allows it to be analyzed across all data fields for purposes of informing and updating clinical practice guidelines of the Department of Veterans Affairs.\n**(B) Compilation of data regarding covered veterans**\nIn compiling data under paragraph (2) regarding covered veterans described in subparagraphs (A) through (C) of such paragraph, data regarding veterans described in each such subparagraph shall be compiled separately and disaggregated by year.\n**(4) Completion of review and report**\nThe agreement entered into under paragraph (1) shall require that the National Academies of Sciences, Engineering, and Medicine complete the review under such paragraph and submit to the Secretary of Veterans Affairs a report containing the results of the review not later than 180 days after entering into the agreement.\n##### (b) Report\nNot later than 30 days after the completion by the National Academies of Sciences, Engineering, and Medicine of the review required under subsection (a), the Secretary of Veterans Affairs shall\u2014\n**(1)**\nsubmit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the results of the review; and\n**(2)**\nmake such report publicly available.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term black box warning means a warning displayed on the label of a prescription drug that is designed to call attention to the serious or life-threatening risk of the prescription drug.\n**(2)**\nThe term covered veteran means a veteran who received hospital care or medical services furnished by the Department of Veterans Affairs during the five-year period preceding the death of the veteran.\n**(3)**\nThe term first-line treatment means a potential intervention that has been evaluated and assigned a high score within clinical practice guidelines.\n**(4)**\nThe term State means each of the States, territories, and possessions of the United States, the District of Columbia, and the Commonwealth of Puerto Rico.",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-06T15:22:19Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Marriage and family status",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-02-06T15:22:19Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-02-06T15:22:18Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-02-06T15:22:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-01-31T16:50:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr136",
          "measure-number": "136",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr136v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veteran Overmedication and Suicide Prevention Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to contract with the National Academies of Sciences, Engineering, and Medicine to report on the deaths of covered veterans who died by suicide during the last five years, regardless of whether information relating to such deaths has been reported by the Centers for Disease Control and Prevention. A covered veteran is any veteran who received VA hospital care or medical services during the five-year period preceding the veteran's death.</p><p>Among other elements, the report shall include the total number of covered veterans who died by suicide, violent death, or accidental death, as well as certain demographic information.</p>"
        },
        "title": "Veteran Overmedication and Suicide Prevention Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr136.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veteran Overmedication and Suicide Prevention Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to contract with the National Academies of Sciences, Engineering, and Medicine to report on the deaths of covered veterans who died by suicide during the last five years, regardless of whether information relating to such deaths has been reported by the Centers for Disease Control and Prevention. A covered veteran is any veteran who received VA hospital care or medical services during the five-year period preceding the veteran's death.</p><p>Among other elements, the report shall include the total number of covered veterans who died by suicide, violent death, or accidental death, as well as certain demographic information.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr136"
    },
    "title": "Veteran Overmedication and Suicide Prevention Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veteran Overmedication and Suicide Prevention Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to contract with the National Academies of Sciences, Engineering, and Medicine to report on the deaths of covered veterans who died by suicide during the last five years, regardless of whether information relating to such deaths has been reported by the Centers for Disease Control and Prevention. A covered veteran is any veteran who received VA hospital care or medical services during the five-year period preceding the veteran's death.</p><p>Among other elements, the report shall include the total number of covered veterans who died by suicide, violent death, or accidental death, as well as certain demographic information.</p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr136"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr136ih.xml"
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
      "title": "Veteran Overmedication and Suicide Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veteran Overmedication and Suicide Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T10:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to conduct an independent review of the deaths of certain veterans by suicide, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T10:48:26Z"
    }
  ]
}
```
