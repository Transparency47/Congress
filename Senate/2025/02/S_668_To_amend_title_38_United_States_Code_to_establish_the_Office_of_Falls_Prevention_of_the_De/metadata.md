# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/668?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/668
- Title: SAFE STEPS for Veterans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 668
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-12-11T12:03:16Z
- Update date including text: 2025-12-11T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/668",
    "number": "668",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "SAFE STEPS for Veterans Act of 2025",
    "type": "S",
    "updateDate": "2025-12-11T12:03:16Z",
    "updateDateIncludingText": "2025-12-11T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
            "date": "2025-12-10T21:00:02Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-20T19:41:24Z",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "SD"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s668is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 668\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. King (for himself and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish the Office of Falls Prevention of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Access to Falls Education and Prevention and Strengthening Training Efforts and Promoting Safety Initiatives for Veterans Act of 2025 or the SAFE STEPS for Veterans Act of 2025 .\n#### 2. Establishment of Office of Falls Prevention of Department of Veterans Affairs\n##### (a) Establishment of office\n**(1) In general**\nSubchapter I of chapter 73 of title 38, United States Code, is amended by inserting after section 7310A the following new section:\n7310B. Office of Falls Prevention (a) Office (1) Establishment and operation The Under Secretary for Health shall establish and operate in the Veterans Health Administration the Office of Falls Prevention (in this section referred to as the Office ). (2) Location of office The Office shall be located at the Central Office of the Department. (3) Leadership (A) Head The head of the Office is the Chief Officer of Falls Prevention (in this section referred to as the Chief Officer ). (B) Reporting The Chief Officer shall report to the Under Secretary for Health. (4) Staffing and support The Under Secretary for Health shall provide the Office with such staff and other support as may be necessary for the Office to carry out effectively the functions of the Office under this section. (5) Reorganization The Under Secretary for Health may reorganize existing offices within the Veterans Health Administration as of the date of the enactment of this section in order to avoid duplication with the functions of the Office. (b) Functions The functions of the Office include the following: (1) To provide a central office for monitoring and encouraging the activities of the Veterans Health Administration with respect to the provision, evaluation, and improvement of health care services relating to falls prevention provided to veterans by the Department, with the goal of averting costly health care utilization while decreasing the incidence of falls. (2) To develop and implement standards of care for the provision by the Department of health care services relating to falls prevention. (3) To monitor and identify deficiencies in standards of care for the provision of health care services relating to falls prevention, to provide technical assistance to medical facilities of the Department, to provide technical assistance to programs of the Department that support veterans in their own homes, to address and remedy deficiencies of such facilities and programs, and to perform oversight of implementation of such standards of care. (4) To monitor and identify deficiencies in standards of care for the provision of health care services relating to falls prevention through the community pursuant to this title and to provide recommendations to the appropriate office to address and remedy any deficiencies. (5) To oversee distribution of resources and information related to falls prevention for veterans under this title. (6) To promote the expansion and improvement of clinical, research, and educational activities of the Veterans Health Administration with respect to health care services relating to falls prevention, including research activities on falls prevention conducted between the Office of Research and Development of the Department and the National Institute on Aging. (7) To promote the development or expansion of rigorous quality assessment or improvement processes designed to prevent falls, including through coordination and collaboration with offices within the Department determined appropriate by the Secretary. (8) To coordinate home modification and adaptation programs administered by the Under Secretary for Benefits under chapter 21 of this title and the Under Secretary for Health under section 1717(a)(2) of this title. (9) To carry out such other duties as the Under Secretary for Health may require. (c) Public education campaign The Chief Officer shall\u2014 (1) oversee and support a national education campaign that\u2014 (A) is directed principally to veterans determined to be at risk for falls, their families, and their health care providers; and (B) focuses on\u2014 (i) reducing falls, falls with major injury, and repeat falls for veterans receiving care under the laws administered by the Secretary; and (ii) increasing awareness of available benefits, grants, devices, or services provided by the Department that would aid veterans in reducing falls and preventing repeat falls; and (2) award grants or contracts to qualified organizations for the purpose of supporting local education campaigns focusing on reducing falls, falls with major injury, and repeat falls for veterans receiving care under the laws administered by the Secretary. (d) Research on falls prevention programs for veteran populations (1) In general The Chief Officer shall work with the Office of Research and Development of the Department and the National Institute on Aging to develop research for evidence-based falls prevention programs that will benefit veterans, including\u2014 (A) programs that overlap with the priorities of the Department; (B) programs that may focus on or be of particular benefit to veterans; and (C) programs that may include participants with multiple comorbidities. (2) Matters To be included The research required under paragraph (1) shall include the following: (A) Research in supporting veterans with and without service-connected disabilities receiving home modification grants under section 1717 or 2101 of this title. (B) Development of recommendations for falls prevention interventions for veterans with service-connected disabilities, including home modification interventions. (C) Research addressing medication management and polypharmacy as risk factors for falls prevention and developing recommendations for providers and electronic health records systems of the Department to monitor for veterans at risk of falls based on use of certain medications. (D) Research on improvements for safe patient handling and mobility among veterans, particularly in facilities (both medical and non-medical) that are not spinal cord injury centers. (3) Subject matter expert panel (A) In general The Secretary and the Director of the National Institute on Aging shall establish a joint subject matter expert panel to develop recommendations as required under paragraph (2)(B). (B) Membership The subject matter expert panel required under subparagraph (A) shall be comprised of eight members, of which\u2014 (i) four shall be appointed by the Secretary; and (ii) four shall be appointed by the Director of the National Institute on Aging. .\n**(2) Establishment of joint subject matter expert panel**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs and the Director of the National Institute on Aging shall establish the joint subject matter expert panel required under section 7310B(d)(3) of title 38, United States Code, as added by paragraph (1).\n**(3) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 7310A the following new item:\n7310B. Office of Falls Prevention. .\n##### (b) Expansion of Interagency Coordinating Committee on Healthy Aging and Age-Friendly Communities\nSection 203(c) of the Older Americans Act of 1965 ( 42 U.S.C. 3013(c) ) is amended\u2014\n**(1)**\nin paragraph (2), by inserting the Secretary of Veterans Affairs, after the Commissioner of Social Security, ; and\n**(2)**\nin paragraph (7), in the matter preceding subparagraph (A)\u2014\n**(A)**\nby inserting the Committee on Veterans\u2019 Affairs of the House of Representatives, after the Committee on Ways and Means of the House of Representatives, ; and\n**(B)**\nby inserting the Committee on Veterans\u2019 Affairs of the Senate, after the Committee on Health, Education, Labor, and Pensions of the Senate, .\n##### (c) Safe handling transfer techniques\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall issue or update directives of the Veterans Health Administration for facilities and providers relating to safe patient handling and mobility policies at the national, Veterans Integrated Service Network, and health-care system levels, which shall include the following:\n**(1)**\nRequiring biennial training for providers, including that all providers be trained in safe patient handling and use of mobility aids and mobility techniques.\n**(2)**\nRequiring that any medical facility where patients may need assistance with transfer or mobility have access to safe patient handling and mobility technology appropriate for the setting to enable safe transfer and mobilization for access to care and activities of daily living for veterans who are paralyzed or who need assistance with mobility.\n**(3)**\nRequiring that all emergency settings have immediate access to safe patient handling and mobility technology to enable safe transfer, fall recovery, and repositioning.\n##### (d) Pilot program on falls prevention interventions tied to residential adaptations and alterations\n**(1) Determination**\nThe Secretary of Veterans Affairs shall determine the feasibility and advisability of carrying out a pilot program to provide home improvements and structural alterations to prevent falls for all veterans eligible for those services under the laws administered by the Secretary.\n**(2) Plan**\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to Congress a report\u2014\n**(A)**\nindicating the plans of the Secretary to carry out a pilot program to provide home improvements and structural alterations to prevent falls for all veterans eligible for those services under the laws administered by the Secretary; or\n**(B)**\nspecifying why the Secretary determined under paragraph (1) that it is not feasible or advisable to carry out such a pilot program.\n**(3) Report on lessons learned**\nIf the Secretary carries out the pilot program described in paragraph (1), not later than 180 days after the termination of the pilot program, the Chief Officer of Falls Prevention of the Department of Veterans Affairs established under section 7310B(a)(3)(A) of title 38, United States Code, as added by subsection (a)(1), shall submit to Congress a report on lessons learned from the pilot program and any recommendations on extending or expanding the pilot program.\n##### (e) Report on falls prevention initiatives\n**(1) In general**\nNot later than two years after the date of the enactment of this Act, or one year after the appointment of the Chief Officer of Falls Prevention of the Department of Veterans Affairs established under section 7310B(a)(3)(A) of title 38, United States Code, as added by subsection (a)(1), whichever occurs first, the Chief Officer, or the Under Secretary for Health of the Department of Veterans Affairs if a Chief Officer has not yet been appointed, shall submit to Congress a report on falls prevention initiatives within the Department.\n**(2) Elements**\nThe report required by paragraph (1) shall evaluate, for the three-year period preceding the date of the enactment of this Act\u2014\n**(A)**\nscreening procedures at facilities of the Veterans Health Administration for risk of falls and the prevalence of resulting falls prevention interventions;\n**(B)**\nthe use by the Department of electronic health record documentation for risk of falls among veterans;\n**(C)**\nthe number of home modification grants provided under either the Home Improvements and Structural Alterations Program of the Department under section 1717 of title 38, United States Code, or the Specially Adapted Housing Program of the Department under section 2101 of such title;\n**(D)**\nthe extent to which grants provided under the programs specified under subparagraph (C) prevent falls among veterans and any recommendations with respect to such programs in the case of falls among veterans that were not prevented;\n**(E)**\nfor veterans eligible for the Home Improvements and Structural Alterations Program of the Department under section 1717 of title 38, United States Code, pursuant to subsection (a)(2)(B) of such section, the number of home modification grants provided to each veteran in receipt of such a grant;\n**(F)**\nthe types of providers that have conducted medical assessments leading to a recommendation for a home modification tied to medical necessity, and any recommendations for legislative or administrative action to expand the list of providers eligible to conduct medical assessments leading to a recommendation for a home modification;\n**(G)**\nhome evaluation processes that are conducted in connection with awards made under the programs specified under subparagraph (C) and any recommendations for improving the evaluation and review process;\n**(H)**\nreporting programs and software of the Department used to capture incidences of falls in care sites of the Veterans Health Administration and other veterans' settings;\n**(I)**\nlimitations on uptake and use of current prevention, screening, and intervention programs designed to address falls prevention; and\n**(J)**\nrecommendations for the Secretary of Veterans Affairs to work with the Centers for Disease Control and Prevention, or other entities determined appropriate by the Secretary, to better capture data on falls by a veteran occurring in the home or in the community.\n#### 3. Establishment of falls assessment and fall prevention service requirements for veterans\n##### (a) Required nursing home care\nSection 1710A of title 38, United States Code, is amended by striking subsection (d) and inserting the following:\n(d) In the case of an individual determined by a physician to have fallen or to have been at risk of falling during the previous one-year period, the Secretary shall ensure that a licensed physical therapist or a licensed occupational therapist conducts a falls risk assessment for the individual and provides fall prevention services during the stay of the individual in the nursing home. (e) The provisions of subsection (a) shall terminate on September 30, 2028. .\n##### (b) Extended care services\nSection 1710B(a) of such title is amended by adding at the end the following new paragraph:\n(7) The conduct of an annual falls risk assessment and the provision of fall prevention services by a licensed physical therapist or licensed occupational therapist. .",
      "versionDate": "2025-02-20",
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
        "actionDate": "2025-05-05",
        "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3183",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAFE STEPS for Veterans Act of 2025",
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
            "name": "Aging",
            "updateDate": "2025-07-10T17:32:24Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-10T17:33:26Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-07-10T17:32:33Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-10T17:32:37Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-07-10T17:33:37Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-10T17:32:29Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-07-10T17:33:30Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-07-10T17:32:42Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-07-10T17:32:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T17:29:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s668",
          "measure-number": "668",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s668v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supporting Access to Falls Education and Prevention and Strengthening Training Efforts and Promoting Safety Initiatives for Veterans Act of 2025 or the SAFE STEPS for Veterans Act of 2025</strong></p><p>This bill addresses certain mobility and aging care and services provided by the Department of Veterans Affairs (VA).</p><p>First, the bill requires the establishment and operation of the Office of Falls Prevention within the Veterans Health Administration (VHA) for purposes of providing, evaluating, and improving VA health care services related to falls prevention.</p><p>Among other duties, the office must oversee and support a national education campaign for veterans, their families, and health care providers that focuses on reducing falls and increases awareness of available benefits or services provided by the VA to reduce falls.</p><p>The bill also expands membership of the Interagency Coordinating Committee on Healthy Aging and Age-Friendly Communities by including the VA.</p><p>The VA must issue or update directives of the VHA for facilities and providers relating to safe patient handling and mobility policies.</p><p>Additionally, the VA must determine the feasibility and advisability of implementing a pilot program to provide home improvements and structural alterations to prevent falls for veterans who are eligible for such services under VA laws.</p><p>Finally, the bill requires the VA to ensure certain veterans receive a falls risk assessment from a licensed physical therapist or occupational therapist.</p>"
        },
        "title": "SAFE STEPS for Veterans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s668.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Access to Falls Education and Prevention and Strengthening Training Efforts and Promoting Safety Initiatives for Veterans Act of 2025 or the SAFE STEPS for Veterans Act of 2025</strong></p><p>This bill addresses certain mobility and aging care and services provided by the Department of Veterans Affairs (VA).</p><p>First, the bill requires the establishment and operation of the Office of Falls Prevention within the Veterans Health Administration (VHA) for purposes of providing, evaluating, and improving VA health care services related to falls prevention.</p><p>Among other duties, the office must oversee and support a national education campaign for veterans, their families, and health care providers that focuses on reducing falls and increases awareness of available benefits or services provided by the VA to reduce falls.</p><p>The bill also expands membership of the Interagency Coordinating Committee on Healthy Aging and Age-Friendly Communities by including the VA.</p><p>The VA must issue or update directives of the VHA for facilities and providers relating to safe patient handling and mobility policies.</p><p>Additionally, the VA must determine the feasibility and advisability of implementing a pilot program to provide home improvements and structural alterations to prevent falls for veterans who are eligible for such services under VA laws.</p><p>Finally, the bill requires the VA to ensure certain veterans receive a falls risk assessment from a licensed physical therapist or occupational therapist.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119s668"
    },
    "title": "SAFE STEPS for Veterans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Access to Falls Education and Prevention and Strengthening Training Efforts and Promoting Safety Initiatives for Veterans Act of 2025 or the SAFE STEPS for Veterans Act of 2025</strong></p><p>This bill addresses certain mobility and aging care and services provided by the Department of Veterans Affairs (VA).</p><p>First, the bill requires the establishment and operation of the Office of Falls Prevention within the Veterans Health Administration (VHA) for purposes of providing, evaluating, and improving VA health care services related to falls prevention.</p><p>Among other duties, the office must oversee and support a national education campaign for veterans, their families, and health care providers that focuses on reducing falls and increases awareness of available benefits or services provided by the VA to reduce falls.</p><p>The bill also expands membership of the Interagency Coordinating Committee on Healthy Aging and Age-Friendly Communities by including the VA.</p><p>The VA must issue or update directives of the VHA for facilities and providers relating to safe patient handling and mobility policies.</p><p>Additionally, the VA must determine the feasibility and advisability of implementing a pilot program to provide home improvements and structural alterations to prevent falls for veterans who are eligible for such services under VA laws.</p><p>Finally, the bill requires the VA to ensure certain veterans receive a falls risk assessment from a licensed physical therapist or occupational therapist.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119s668"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s668is.xml"
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
      "title": "SAFE STEPS for Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE STEPS for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting Access to Falls Education and Prevention and Strengthening Training Efforts and Promoting Safety Initiatives for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to establish the Office of Falls Prevention of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:24Z"
    }
  ]
}
```
