# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/609?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/609
- Title: BRAVE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 609
- Origin chamber: Senate
- Introduced date: 2025-02-18
- Update date: 2026-04-28T11:03:21Z
- Update date including text: 2026-04-28T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in Senate
- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-02-18: Introduced in Senate

## Actions

- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/609",
    "number": "609",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "BRAVE Act of 2025",
    "type": "S",
    "updateDate": "2026-04-28T11:03:21Z",
    "updateDateIncludingText": "2026-04-28T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-18",
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
            "date": "2025-02-18T21:10:36Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-18T21:10:36Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NH"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-01-14",
      "state": "ME"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s609is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 609\nIN THE SENATE OF THE UNITED STATES\nFebruary 18, 2025 Mr. Blumenthal introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo improve mental health services of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Building Resources and Access for Veterans' Mental Health Engagement Act of 2025 or the BRAVE Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Improvement of workforce in support of mental health care\nSec. 101. Report on market pay surveys for Readjustment Counseling Service positions.\nSec. 102. Qualifications of appointees in occupations that support mental health programs.\nSec. 103. Report on coordination of Veterans Health Administration with Readjustment Counseling Service.\nTITLE II\u2014Improvement of Vet Center infrastructure and technology\nSec. 201. Vet Center defined.\nSec. 202. Comptroller General report on Readjustment Counseling Service model for expansion of Vet Center footprint.\nSec. 203. Improvement of guidance and information to improve veteran outreach efforts by Vet Centers.\nSec. 204. Report on information technology system of Readjustment Counseling Service.\nTITLE III\u2014Women veterans\nSec. 301. Study on effectiveness of suicide prevention and mental health outreach programs of Department of Veterans Affairs for women veterans.\nSec. 302. Requirement for Department of Veterans Affairs to modify the REACH VET program to incorporate risk factors weighted for women veterans.\nSec. 303. Review of and report on reintegration and readjustment services for veterans and family members in group retreat settings.\nTITLE IV\u2014Other matters\nSec. 401. Extension of Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program.\nSec. 402. Access to mental health residential rehabilitation treatment programs for veterans with spinal cord injury or disorder.\nSec. 403. Mental health consultations and outreach on mental health services for veterans receiving compensation for disabilities relating to mental health diagnoses.\nSec. 404. Joint report on effectiveness of programs of Department of Veterans Affairs and Department of Defense that promote access to mental health services for transitioning members of the Armed Forces.\nI\nImprovement of workforce in support of mental health care\n#### 101. Report on market pay surveys for Readjustment Counseling Service positions\n##### (a) Findings\nCongress finds that the Secretary of Veterans Affairs, through the Chief Readjustment Counseling Officer, reviews market pay surveys in each Readjustment Counseling Service District to compare the salaries of employees in the Readjustment Counseling Service of the Department of Veterans Affairs, including licensed professional mental health counselors, social workers, and marriage and family therapists, to the salaries of similarly situated employees within the Department and the private sector.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the findings specified in subsection (a), which shall\u2014\n**(1)**\ninclude an assessment of pay disparities between employees of the Readjustment Counseling Service of the Department and similarly situated employees within the Department and the private sector; and\n**(2)**\nidentify if pay-related staffing challenges exist, and if so, determine if each Readjustment Counseling Service District has initiated a review of third-party survey data for the identified occupations.\n##### (c) Districts\nEach report submitted under subsection (b) shall include reports from all Readjustment Counseling Service Districts of the Department, including\u2014\n**(1)**\nareas that are geographically diverse;\n**(2)**\nrural areas;\n**(3)**\nhighly rural areas;\n**(4)**\nurban areas; and\n**(5)**\nareas with health care shortages.\n##### (d) Assessment of pay\nEach report submitted under subsection (b) shall include an assessment of pay based on the following factors:\n**(1)**\nThird-party survey data.\n**(2)**\nGeographic location.\n**(3)**\nEquivalent qualifications (licensure, education level, or experience).\n**(4)**\nShort-term incentives.\n#### 102. Qualifications of appointees in occupations that support mental health programs\n##### (a) Psychologists\nSection 7402(b)(8)(C) of title 38, United States Code, is amended by striking for a period not to exceed and all that follows through the period at the end and inserting for a reasonable period of time recommended by the Under Secretary for Health. .\n##### (b) Licensed professional mental health counselors\nSection 7402(b)(11)(B) of title 38, United States Code, is amended by striking the period at the end and inserting , except that the Secretary may waive the requirement of licensure or certification for an individual licensed professional mental health counselor for a reasonable period of time recommended by the Under Secretary for Health. .\n#### 103. Report on coordination of Veterans Health Administration with Readjustment Counseling Service\n##### (a) In general\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report regarding coordination between the clinical care system of the Veterans Health Administration and the Readjustment Counseling Service of the Department of Veterans Affairs.\n##### (b) Assessment\nThe report required by subsection (a) shall include an assessment of the adherence by each Director of a Veterans Integrated Service Network to policies of the Veterans Health Administration, which require each such Director to ensure that a support facility of the Department of Veterans Affairs is aligned laterally with each Vet Center to provide supportive administrative and clinical collaboration to better serve veterans eligible for services from Vet Centers, particularly those at high risk for suicide.\n##### (c) Analysis\nThe report required by subsection (a) shall include an analysis of\u2014\n**(1)**\nwhether staff at Vet Centers in the local area of a medical facility of the Department have the updated contact information for appropriate staff at the medical facility to ensure proper coordination of care;\n**(2)**\nwhether the external clinical consultant and suicide prevention coordinator of a medical facility of the Department are providing counseling staff of each Vet Center in the local area of the medical facility professional consultation not less frequently than monthly through regularly scheduled peer case presentations onsite at the Vet Center or via virtual or telephone consultation as necessary to fully support the coordination of care of patients, particularly those at high risk for suicide;\n**(3)**\nwhether the external clinical consultant and suicide prevention coordinator are documenting any consultation conducted under paragraph (2); and\n**(4)**\nwhether the Under Secretary for Health is coordinating with the Outreach Specialist at each Vet Center to ensure active duty members of the Armed Forces who are participating in the Transition Assistance Program of the Department of Defense are provided information regarding Vet Centers and the services provided at Vet Centers.\n##### (d) Vet Center defined\nIn this section, the term Vet Center has the meaning given that term in section 1712A(h) of title 38, United States Code.\nII\nImprovement of Vet Center infrastructure and technology\n#### 201. Vet Center defined\nIn this title, the term Vet Center has the meaning given that term in section 1712A(h) of title 38, United States Code.\n#### 202. Comptroller General report on Readjustment Counseling Service model for expansion of Vet Center footprint\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report assessing the model used by the Readjustment Counseling Service of the Department of Veterans Affairs to guide the expansion of the real property footprint of Vet Centers.\n##### (b) Elements\nThe report required by subsection (a) shall assess\u2014\n**(1)**\nwhether the model described in such subsection adequately accounts for the demand for Vet Center services in rural areas;\n**(2)**\nwhether the frequency with which the Secretary of Veterans Affairs is reassessing areas for potential expansion of Vet Center services is often enough to address any population shifts;\n**(3)**\nwhether such model adequately considers the needs of veterans in areas with high rates of calls to the Veterans Crisis Line or high rates of suicide by veterans or members of the Armed Forces;\n**(4)**\nwhether such model adequately accounts for trends in usage of mobile Vet Centers in a given area; and\n**(5)**\nwhether such model takes into account the unique needs of veterans and members of the Armed Forces in areas being assessed.\n##### (c) Veterans Crisis Line\nIn this section, the term Veterans Crisis Line means the toll-free hotline for veterans established under section 1720F(h) of title 38, United States Code.\n#### 203. Improvement of guidance and information to improve veteran outreach efforts by Vet Centers\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall\u2014\n**(1)**\nensure each Vet Center has demographic data, such as age, gender, race, and ethnicity, for individuals eligible for Vet Center services in the service area of such Vet Center to be used to tailor outreach activities, including data on veterans who have recently transitioned from service in the Armed Forces;\n**(2)**\nprovide Vet Centers with guidance for assessing the effectiveness of outreach activities, including guidance on metrics for those activities and targets against which to assess those metrics to determine effectiveness;\n**(3)**\ndevelop and implement a process to periodically assess the extent to which veterans and members of the Armed Forces who are eligible for services from Vet Centers experience barriers to obtaining such services, including a lack of awareness about Vet Centers and challenges accessing Vet Center services; and\n**(4)**\ndevelop and implement a process to periodically assess the extent to which staff of Vet Centers may encounter barriers to providing services.\n#### 204. Report on information technology system of Readjustment Counseling Service\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Veterans Affairs, through the Chief Readjustment Counseling Officer of the Veterans Health Administration, shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report identifying\u2014\n**(1)**\nwhether the Department of Veterans Affairs is retaining or replacing the current information technology platform of the Department, commonly referred to as RCSNet , which is currently used to manage certain parts of the daily work of employees of the Readjustment Counseling Service and operational data and management functions of the Readjustment Counseling Service;\n**(2)**\nif the Department intends to keep RCSNet, the rationale for that decision and an identification of the steps the Department is taking to maintain or improve the functionality of RCSNet and the timeline for those steps; and\n**(3)**\nif the Department intends to replace RCSNet, the rationale for that decision and an identification of the steps the Department is taking to implement that replacement, including a timeline and the estimated cost for that replacement.\nIII\nWomen veterans\n#### 301. Study on effectiveness of suicide prevention and mental health outreach programs of Department of Veterans Affairs for women veterans\n##### (a) In general\nNot later than 240 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall conduct surveys and host listening sessions with women veterans to determine the extent to which\u2014\n**(1)**\nsuicide prevention, lethal-means safety, and mental health resources and messaging campaigns of the Department of Veterans Affairs are perceived and accepted by women veterans;\n**(2)**\nwomen veterans find those resources and messaging campaigns effective and sufficiently tailored to women veterans;\n**(3)**\nthe integration into those resources and messaging campaigns of information pertaining to military sexual trauma, intimate partner violence, and trauma-informed health care would make those resources and messaging campaigns more effective for women veterans;\n**(4)**\nthe Department could make additional improvements to those resources and messaging campaigns, including the Women\u2019s Health Transition Training Program, to make those resources and messaging campaigns more effective for women veterans; and\n**(5)**\nprograms and services of the Department are targeted at women veterans of different ages and eras of services, racial and ethnic backgrounds, and geographical areas.\n##### (b) Population studied\nThe Secretary shall conduct the surveys and listening sessions required under subsection (a) in urban and rural areas and shall ensure such surveys and listening sessions are targeted at different demographics.\n##### (c) Report\nNot later than one year after the surveys and listening sessions required under subsection (a) are complete, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the findings of such surveys and listening sessions, which shall document the steps the Secretary intends to take to refine the suicide prevention, lethal-means safety, and mental health resources and messaging campaigns of the Department based on the feedback from such surveys and listening sessions to ensure the Secretary is utilizing the most effective strategies.\n#### 302. Requirement for Department of Veterans Affairs to modify the REACH VET program to incorporate risk factors weighted for women veterans\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall initiate efforts to modify the Recovery Engagement and Coordination for Health\u2013Veterans Enhanced Treatment program ( REACH VET ) to incorporate into such program risk factors weighted for women, such as military sexual trauma and intimate partner violence.\n#### 303. Review of and report on reintegration and readjustment services for veterans and family members in group retreat settings\n##### (a) Review\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall review all requests for reintegration and readjustment services for veterans and family members of veterans in group retreat program settings under section 1712A(a)(1)(B)(ii) of title 38, United States Code, to determine if current retreat programming meets demand, specifically requests for\u2014\n**(1)**\nwomen only retreats;\n**(2)**\ndisabled access retreats, particularly wheelchair accessible retreats; and\n**(3)**\nretreats for veterans with specific medical needs.\n##### (b) Report\nNot later than 120 days after the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on whether the provision by the Secretary of reintegration and readjustment services for veterans and family members of veterans in group retreat program settings should be increased and made permanent, including\u2014\n**(1)**\nwomen only retreats;\n**(2)**\ndisabled access retreats, particularly wheelchair accessible retreats; and\n**(3)**\nretreats for veterans with specific medical needs.\nIV\nOther matters\n#### 401. Extension of Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program\nSection 201 of the Commander John Scott Hannon Veterans Mental Health Care Improvement Act of 2019 ( Public Law 116\u2013171 ; 38 U.S.C. 1720F note) is amended\u2014\n**(1)**\nin subsection (c)(2)(A), by striking $750,000 and inserting $1,000,000 ; and\n**(2)**\nin subsection (j), by striking three years and inserting six years .\n#### 402. Access to mental health residential rehabilitation treatment programs for veterans with spinal cord injury or disorder\n##### (a) Plan\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a plan to ensure access to mental health residential treatment programs of the Department of Veterans Affairs for veterans with a spinal cord injury or disorder.\n**(2) Elements**\nThe plan required under paragraph (1) shall include\u2014\n**(A)**\na staffing plan, which shall include a plan for how the Department will\u2014\n**(i)**\nincorporate staff from other facilities to support the pilot program required under subsection (b); and\n**(ii)**\nensure adequate staffing to support the needs of veterans with a spinal cord injury or disorder;\n**(B)**\nan assessment of medical equipment needs; and\n**(C)**\nan assessment of the best location to deliver treatment and health care under the mental health residential treatment programs of the Department, including through the use of spinal cord injury or disorder centers and spinal cord injury or disorder spokes.\n##### (b) Pilot program\nCommencing not later than 120 days after the date of the enactment of this Act, the Secretary shall carry out a pilot program to provide access to mental health residential treatment programs of the Department for veterans with a spinal cord injury or disorder at not fewer than three medical facilities of the Department.\n##### (c) Report\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on\u2014\n**(1)**\nthe implementation of the plan required under subsection (a);\n**(2)**\nthe initial results from the pilot program under subsection (b); and\n**(3)**\nplans to expand the mental health residential treatment programs of the Department to additional medical facilities of the Department to address demand for the highly specialized treatment provided under such programs for veterans with a spinal cord injury or disorder.\n#### 403. Mental health consultations and outreach on mental health services for veterans receiving compensation for disabilities relating to mental health diagnoses\n##### (a) Technical corrections\n**(1) In general**\nThe section 1167 of title 38, United States Code, relating to mental health consultations, is redesignated as section 1169.\n**(2) Clerical amendments**\nThe table of sections at the beginning of chapter 11 is amended\u2014\n**(A)**\nby striking the item relating to the section 1167 relating to mental health consultations; and\n**(B)**\nadding after the item relating to section 1168 the following new item:\n1169. Mental health consultations. .\n##### (b) Improvements\nSection 1169 of such title, as redesignated by subsection (a), is amended\u2014\n**(1)**\nin subsection (a), in the subsection heading, by striking In general and inserting Initial mental health consultations ;\n**(2)**\nby redesignating subsection (b) and (c) as subsections (c) and (d), respectively;\n**(3)**\nby inserting after subsection (a) the following new subsection (b):\n(b) Annual mental health consultations and outreach Not less frequently than once each year, the Secretary shall\u2014 (1) offer to each veteran who is receiving compensation under this chapter for a service-connected disability relating to a mental health diagnosis a mental health consultation to assess the mental health needs of, and discuss other mental health care options for, the veteran; and (2) conduct outreach to each veteran described in paragraph (1) regarding the availability of consultations described in such paragraph and other mental health services from the Department. ;\n**(4)**\nin subsection (c), as redesignated by paragraph (2), by inserting or (b) after under subsection (a) both places it appears; and\n**(5)**\nin subsection (d), as redesignated by paragraph (2), by inserting or as requiring reevaluation of any entitlement of the veteran to compensation under this chapter before the period at the end.\n##### (c) Biennial reports\nSuch section, as amended by subsection (b), is further amended by adding at the end the following new subsection:\n(e) Biennial reviews and reports (1) Not later than one year after the date of the enactment of the BRAVE Act of 2025 , and not less frequently than once every two years thereafter, the Secretary shall\u2014 (A) review the efficacy of the outreach of the Department with respect to consultations offered under this section; and (B) submit to the Committee on Veterans' Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives a report on\u2014 (i) the findings of the Secretary with respect to the most recent review conducted pursuant to subparagraph (A); and (ii) the plans of the Secretary to address the findings described in clause (i). (2) In order to facilitate reviews conducted under paragraph (1)(A), the Secretary shall\u2014 (A) ensure veterans can provide feedback to the Secretary on outreach described in paragraph (1) and the consultations offered under this section; and (B) analyze the feedback described in subparagraph (A) that is provided to the Secretary. (3) Each review conducted pursuant to paragraph (1)(A) shall cover the following: (A) The feedback collected under paragraph (2). (B) Consultations sought pursuant to offers under this section. (C) Matters that deter veterans from seeking consultations offered under this section. .\n#### 404. Joint report on effectiveness of programs of Department of Veterans Affairs and Department of Defense that promote access to mental health services for transitioning members of the Armed Forces\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs and the Secretary of Defense shall jointly submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the actions taken or that will be taken by each such Secretary, either independently or jointly, to improve the effectiveness of programs of the Department of Veterans Affairs and the Department of Defense that promote access to mental health services for members of the Armed Forces transitioning from service in the Armed Forces to civilian life.\n##### (b) Status of response to Comptroller General recommendations\nThe report required under subsection (a) shall include an assessment of the status of the response by the Secretary of Veterans Affairs and the Secretary of Defense to the recommendations of the Comptroller General of the United States set forth in the July 2024 report entitled DOD AND VA HEALTH CARE: Actions Needed to Better Facilitate Access to Mental Health Services During Military to Civilian Transitions (GAO\u201324\u2013106189).\n##### (c) Identification of duplicative efforts\nThe report required under subsection (a) shall identify any duplicative efforts or gaps in services and recommend changes to programs of the Department of Veterans Affairs or the Department of Defense to address such duplicative efforts or gaps, including recommendations for legislative action.",
      "versionDate": "2025-02-18",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-03",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "6024",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BRAVE Act of 2025",
      "type": "HR"
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
            "name": "Computers and information technology",
            "updateDate": "2025-07-09T14:50:26Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-09T14:50:59Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-07-09T14:51:25Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-07-09T14:51:30Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-09T14:50:36Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-07-09T14:51:15Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-09T14:51:21Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-09T14:50:41Z"
          },
          {
            "name": "Labor market",
            "updateDate": "2025-07-09T14:51:05Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-07-09T14:44:26Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-07-09T14:51:36Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-07-09T14:50:47Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-07-09T14:44:32Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-07-09T14:50:54Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-07-09T14:51:10Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-07-09T14:50:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T17:28:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119s609",
          "measure-number": "609",
          "measure-type": "s",
          "orig-publish-date": "2025-02-18",
          "originChamber": "SENATE",
          "update-date": "2026-01-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s609v00",
            "update-date": "2026-01-06"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Building Resources and Access for Veterans' Mental Health Engagement Act of 2025 or the BRAVE Act of 2025</strong></p><p>This bill addresses mental health services and care provided by the Department of Veterans Affairs (VA), including matters related to personnel, Vet Center administration, care for women veterans, and access to care.</p><p>The bill authorizes the VA to waive the licensure or certification requirement for individual licensed professional mental health counselor appointees for a reasonable period of time.</p><p>The bill also extends the Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program and increases the maximum annual grant amount.</p><p>The VA must provide Vet Centers with guidance for assessing outreach activities and implement processes to periodically assess the extent to which (1) veterans and eligible members of the Armed Forces experience barriers to obtaining services at Vet Centers, and (2) Vet Center staff may encounter barriers to providing services.</p><p>Among other requirements, the VA must also</p><ul><li>survey and host listening sessions with women veterans to gauge the effectiveness of the VA\u2019s suicide prevention, lethal-means safety, and mental health resources and messaging campaigns;</li><li>initiate efforts to modify the Recovery Engagement and Coordination for Health-Veterans Enhanced Treatment (REACH VET) program to incorporate risk factors weighted for women;</li><li>annually offer a mental health consultation to veterans who are receiving compensation for a service-connected disability relating to a mental health diagnosis; and</li><li>implement a pilot program to provide access to mental health residential treatment programs for veterans with a spinal cord injury or disorder.</li></ul>"
        },
        "title": "BRAVE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s609.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Building Resources and Access for Veterans' Mental Health Engagement Act of 2025 or the BRAVE Act of 2025</strong></p><p>This bill addresses mental health services and care provided by the Department of Veterans Affairs (VA), including matters related to personnel, Vet Center administration, care for women veterans, and access to care.</p><p>The bill authorizes the VA to waive the licensure or certification requirement for individual licensed professional mental health counselor appointees for a reasonable period of time.</p><p>The bill also extends the Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program and increases the maximum annual grant amount.</p><p>The VA must provide Vet Centers with guidance for assessing outreach activities and implement processes to periodically assess the extent to which (1) veterans and eligible members of the Armed Forces experience barriers to obtaining services at Vet Centers, and (2) Vet Center staff may encounter barriers to providing services.</p><p>Among other requirements, the VA must also</p><ul><li>survey and host listening sessions with women veterans to gauge the effectiveness of the VA\u2019s suicide prevention, lethal-means safety, and mental health resources and messaging campaigns;</li><li>initiate efforts to modify the Recovery Engagement and Coordination for Health-Veterans Enhanced Treatment (REACH VET) program to incorporate risk factors weighted for women;</li><li>annually offer a mental health consultation to veterans who are receiving compensation for a service-connected disability relating to a mental health diagnosis; and</li><li>implement a pilot program to provide access to mental health residential treatment programs for veterans with a spinal cord injury or disorder.</li></ul>",
      "updateDate": "2026-01-06",
      "versionCode": "id119s609"
    },
    "title": "BRAVE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Building Resources and Access for Veterans' Mental Health Engagement Act of 2025 or the BRAVE Act of 2025</strong></p><p>This bill addresses mental health services and care provided by the Department of Veterans Affairs (VA), including matters related to personnel, Vet Center administration, care for women veterans, and access to care.</p><p>The bill authorizes the VA to waive the licensure or certification requirement for individual licensed professional mental health counselor appointees for a reasonable period of time.</p><p>The bill also extends the Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program and increases the maximum annual grant amount.</p><p>The VA must provide Vet Centers with guidance for assessing outreach activities and implement processes to periodically assess the extent to which (1) veterans and eligible members of the Armed Forces experience barriers to obtaining services at Vet Centers, and (2) Vet Center staff may encounter barriers to providing services.</p><p>Among other requirements, the VA must also</p><ul><li>survey and host listening sessions with women veterans to gauge the effectiveness of the VA\u2019s suicide prevention, lethal-means safety, and mental health resources and messaging campaigns;</li><li>initiate efforts to modify the Recovery Engagement and Coordination for Health-Veterans Enhanced Treatment (REACH VET) program to incorporate risk factors weighted for women;</li><li>annually offer a mental health consultation to veterans who are receiving compensation for a service-connected disability relating to a mental health diagnosis; and</li><li>implement a pilot program to provide access to mental health residential treatment programs for veterans with a spinal cord injury or disorder.</li></ul>",
      "updateDate": "2026-01-06",
      "versionCode": "id119s609"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s609is.xml"
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
      "title": "BRAVE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BRAVE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Building Resources and Access for Veterans' Mental Health Engagement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve mental health services of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:03:28Z"
    }
  ]
}
```
