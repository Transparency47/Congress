# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/139?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/139
- Title: FASD Respect Act
- Congress: 119
- Bill type: S
- Bill number: 139
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-10-23T11:18:15Z
- Update date including text: 2025-10-23T11:18:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/139",
    "number": "139",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "FASD Respect Act",
    "type": "S",
    "updateDate": "2025-10-23T11:18:15Z",
    "updateDateIncludingText": "2025-10-23T11:18:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T21:37:59Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-16",
      "state": "ME"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "HI"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "KS"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "WA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ND"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ME"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "MI"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "GA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s139is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 139\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Ms. Murkowski (for herself, Ms. Klobuchar , Mr. King , Ms. Hirono , Mr. Moran , Ms. Baldwin , Ms. Cantwell , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to reauthorize and extend the Fetal Alcohol Spectrum Disorders Prevention and Services program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing FASD Research, Services and Prevention Act or the FASD Respect Act .\n#### 2. Support for individuals and families impacted by fetal alcohol spectrum disorder\n##### (a) In general\nPart O of title III of the Public Health Service Act ( 42 U.S.C. 280f et seq. ) is amended\u2014\n**(1)**\nby amending the part heading to read as follows: Fetal Alcohol Spectrum Disorders Prevention and Services Program ;\n**(2)**\nin section 399H ( 42 U.S.C. 280f )\u2014\n**(A)**\nin the section heading, by striking Establishment of fetal alcohol syndrome prevention and inserting Fetal alcohol spectrum disorders prevention, intervention, ;\n**(B)**\nby striking Fetal Alcohol Syndrome and Fetal Alcohol Effect each place it appears and inserting FASD ;\n**(C)**\nin subsection (a)\u2014\n**(i)**\nby amending the heading to read as follows: In general ;\n**(ii)**\nin the matter preceding paragraph (1)\u2014\n**(I)**\nby inserting or continue activities to support after shall establish ;\n**(II)**\nby striking FASD (as amended by subparagraph (B)) and inserting fetal alcohol spectrum disorders (referred to in this section as FASD ) ;\n**(III)**\nby striking prevention, intervention and inserting awareness, prevention, identification, intervention, ; and\n**(IV)**\nby striking that shall and inserting , which may ;\n**(iii)**\nin paragraph (1)\u2014\n**(I)**\nin subparagraph (A)\u2014\n**(aa)**\nby striking medical schools and inserting health professions schools ; and\n**(bb)**\nby inserting infants, after provision of services for ; and\n**(II)**\nin subparagraph (D), by striking medical and mental and inserting agencies providing ;\n**(iv)**\nin paragraph (2)\u2014\n**(I)**\nin the matter preceding subparagraph (A), by striking a prevention and diagnosis program to support clinical studies, demonstrations and other research as appropriate and inserting supporting and conducting research on FASD, as appropriate, including ;\n**(II)**\nin subparagraph (B)\u2014\n**(aa)**\nby striking prevention services and interventions for pregnant, alcohol-dependent women and inserting culturally and linguistically appropriate evidence-based or evidence-informed interventions and appropriate societal supports for preventing prenatal alcohol exposure, which may co-occur with exposure to other substances ; and\n**(bb)**\nby striking ; and and inserting a semicolon;\n**(v)**\nby striking paragraph (3) and inserting the following:\n(3) integrating into surveillance a case definition for FASD and, in collaboration with other Federal and outside partners, supporting organizations of appropriate medical and mental health professionals in their development and refinement of evidence-based clinical diagnostic guidelines and criteria for all FASD; and (4) building State and Tribal capacity for the identification, treatment, and support of individuals with FASD and their families, which may include\u2014 (A) utilizing and adapting existing Federal, State, or Tribal programs to include FASD identification and FASD-informed support; (B) developing and expanding screening and diagnostic capacity for FASD; (C) developing, implementing, and evaluating targeted FASD-informed intervention programs for FASD; (D) increasing awareness of FASD; (E) providing training with respect to FASD for professionals across relevant sectors; and (F) disseminating information about FASD and support services to affected individuals and their families. ;\n**(D)**\nin subsection (b)\u2014\n**(i)**\nby striking described in section 399I ;\n**(ii)**\nby striking The Secretary and inserting the following:\n(1) In general The Secretary ; and\n**(iii)**\nby adding at the end the following:\n(2) Eligible entities To be eligible to receive a grant, or enter into a cooperative agreement or contract, under this section, an entity shall\u2014 (A) be a State, Indian Tribe or Tribal organization, local government, scientific or academic institution, or nonprofit organization; and (B) prepare and submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including a description of the activities that the entity intends to carry out using amounts received under this section. (3) Additional application contents The Secretary may require that an eligible entity include in the application submitted under paragraph (2)(B)\u2014 (A) a designation of an individual to serve as a FASD State or Tribal coordinator of activities such eligible entity proposes to carry out through a grant, cooperative agreement, or contract under this section; and (B) a description of an advisory committee the entity will establish to provide guidance for the entity on developing and implementing a statewide or Tribal strategic plan to prevent FASD and provide for the identification, treatment, and support of individuals with FASD and their families. ; and\n**(E)**\nby striking subsections (c) and (d); and\n**(F)**\nby adding at the end the following:\n(c) Definition of FASD-Informed For purposes of this section, the term FASD-informed , with respect to support or an intervention program, means that such support or intervention program uses culturally and linguistically informed evidence-based or practice-based interventions and appropriate societal supports to support an improved quality of life for an individual with FASD and the family of such individual. ; and\n**(3)**\nby striking sections 399I, 399J, and 399K ( 42 U.S.C. 280f\u20131 , 280f\u20132, 280f\u20133) and inserting the following:\n399I. Fetal alcohol spectrum disorders Centers for Excellence (a) In general The Secretary shall, as appropriate, award grants, cooperative agreements, or contracts to public or nonprofit private entities with demonstrated expertise in the prevention of, identification of, and intervention services with respect to, fetal alcohol spectrum disorders (referred to in this section as FASD ) and other related adverse conditions. Such awards shall be for the purposes of establishing Fetal Alcohol Spectrum Disorders Centers for Excellence to build local, Tribal, State, and nationwide capacities to prevent the occurrence of FASD and other related adverse conditions, and to respond to the needs of individuals with FASD and their families by carrying out the programs described in subsection (b). (b) Programs An entity receiving an award under subsection (a) may use such award for the following purposes: (1) Initiating or expanding diagnostic capacity for FASD by increasing screening, assessment, identification, and diagnosis. (2) Developing and supporting public awareness and outreach activities, including the use of a range of media and public outreach, to raise public awareness of the risks associated with alcohol consumption during pregnancy, with the goals of reducing the prevalence of FASD and improving the developmental, health (including mental health), and educational outcomes of individuals with FASD and supporting families caring for individuals with FASD. (3) Acting as a clearinghouse for evidence-based resources on FASD prevention, identification, and culturally and linguistically appropriate best practices, including the maintenance of a national data-based directory on FASD-specific services in States, Indian Tribes, and local communities, and disseminating ongoing research and developing resources on FASD to help inform systems of care for individuals with FASD across their lifespan. (4) Increasing awareness and understanding of efficacious, evidence-based screening tools and culturally and linguistically appropriate evidence-based intervention services and best practices, which may include by conducting nationwide, regional, State, Tribal, or peer cross-State webinars, workshops, or conferences for training community leaders, medical and mental health and substance use disorder professionals, education and disability professionals, families, law enforcement personnel, judges, individuals working in financial assistance programs, social service personnel, child welfare professionals, and other service providers. (5) Improving capacity for State, Tribal, and local affiliates dedicated to FASD awareness, prevention, and identification and family and individual support programs and services. (6) Providing technical assistance to recipients of grants, cooperative agreements, or contracts under section 399H, as appropriate. (7) Carrying out other functions, as appropriate. (c) Application To be eligible for a grant, contract, or cooperative agreement under this section, an entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (d) Subcontracting A public or private nonprofit entity may carry out the following activities required under this section through contracts or cooperative agreements with other public and private nonprofit entities with demonstrated expertise in FASD: (1) Prevention activities. (2) Screening and identification. (3) Resource development and dissemination, training and technical assistance, administration, and support of FASD partner networks. (4) Intervention and treatment services. 399J. Authorization of appropriations There are authorized to be appropriated to carry out this part such sums as may be necessary for each of fiscal years 2025 through 2029. .\n##### (b) Report\nNot later than 4 years after the date of enactment of this Act, the Secretary of Health and Human Services shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives a report on the efforts of the Department of Health and Human Services to advance public awareness of, and facilitate the identification of best practices related to, fetal alcohol spectrum disorders identification, prevention, treatment, and support.\n##### (c) Technical amendment\nSection 519D of the Public Health Service Act ( 42 U.S.C. 290bb\u201325d ) is repealed.",
      "versionDate": "2025-01-16",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child health",
            "updateDate": "2025-03-03T17:35:32Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-03T17:35:32Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-03-03T17:35:32Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-03T17:35:32Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-03T17:35:32Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-03-03T17:35:32Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-03-03T17:35:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T13:50:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "Senate",
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
          "measure-id": "id119s139",
          "measure-number": "139",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s139v00",
            "update-date": "2025-03-25"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Advancing FASD Research, Services and Prevention Act or the FASD Respect Act</strong></p><p>This bill reauthorizes and modifies programs that are administered by\u00a0the Department of Health and Human Services (HHS) to address fetal alcohol spectrum disorders (FASD), including educational and research programs.</p><p>The bill also establishes\u00a0FASD Centers for Excellence to support FASD prevention, such as through screenings, public awareness campaigns, and trainings, particularly at the state and local levels.</p>"
        },
        "title": "FASD Respect Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s139.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Advancing FASD Research, Services and Prevention Act or the FASD Respect Act</strong></p><p>This bill reauthorizes and modifies programs that are administered by\u00a0the Department of Health and Human Services (HHS) to address fetal alcohol spectrum disorders (FASD), including educational and research programs.</p><p>The bill also establishes\u00a0FASD Centers for Excellence to support FASD prevention, such as through screenings, public awareness campaigns, and trainings, particularly at the state and local levels.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119s139"
    },
    "title": "FASD Respect Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Advancing FASD Research, Services and Prevention Act or the FASD Respect Act</strong></p><p>This bill reauthorizes and modifies programs that are administered by\u00a0the Department of Health and Human Services (HHS) to address fetal alcohol spectrum disorders (FASD), including educational and research programs.</p><p>The bill also establishes\u00a0FASD Centers for Excellence to support FASD prevention, such as through screenings, public awareness campaigns, and trainings, particularly at the state and local levels.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119s139"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s139is.xml"
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
      "title": "FASD Respect Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FASD Respect Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing FASD Research, Services and Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to reauthorize and extend the Fetal Alcohol Spectrum Disorders Prevention and Services program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:33:31Z"
    }
  ]
}
```
