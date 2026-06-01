# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3444?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3444
- Title: Tribal Self-Determination and Co-Management in Forestry Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3444
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-07-11T18:30:25Z
- Update date including text: 2025-07-11T18:30:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-06-10 - Committee: Subcommittee Hearings Held
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-06-10 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3444",
    "number": "3444",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "H001068",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Huffman, Jared [D-CA-2]",
        "lastName": "Huffman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Tribal Self-Determination and Co-Management in Forestry Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-11T18:30:25Z",
    "updateDateIncludingText": "2025-07-11T18:30:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-10T16:59:52Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-03T13:58:38Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NM"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CO"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "OR"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "AZ"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "OR"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3444ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3444\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Huffman (for himself, Ms. Leger Fernandez , Mr. Neguse , Ms. Hoyle of Oregon , Ms. Ansari , Ms. Dexter , and Ms. Elfreth ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct Federal land management agencies of the Department of the Interior to establish Tribal Co-Management Plans and to authorize the Secretary of Agriculture to enter into agreements with Indian Tribes and Tribal organizations for the performance of certain activities of the Forest Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tribal Self-Determination and Co-Management in Forestry Act of 2025 .\n#### 2. Tribal Co-Management Plans of the Department of the Interior\n##### (a) In general\nExcept as provided in subsection (c), not later than 1 year after the date of enactment of this Act, the head of each Federal land management agency, in consultation with the Secretary of the Interior and the Tribal Advisory Committee, shall develop a plan, to be known as the Tribal Co-Management Plan of the agency, that includes any activity (including a permissive activity), service, or function (including the management decisions related to such activity, service, or function) of the Federal land management agency that\u2014\n**(1)**\nis to be carried out on lands administered by the Federal land management agency that the Secretary determines are in need of such activity (including restoration activity), service, or function;\n**(2)**\nis consistent with each land management plan of the Federal land management agency;\n**(3)**\nis to be carried out on land that the Secretary, in consultation with each applicable Indian Tribe, identifies as being historically, culturally, or geographically related to such Indian Tribe; and\n**(4)**\nis to be carried out in accordance with applicable laws, including environmental laws and regulations.\n##### (b) Existing Tribal co-Management plans\nIf a plan substantially similar to a plan required under subsection (a) already exists within a Federal land management agency, then not later than 120 days after the date of enactment of this Act, the head of the Federal land management agency shall\u2014\n**(1)**\nadopt such plan as the Tribal Co-Management Plan of the agency; and\n**(2)**\nupdate the plan as necessary to limit, to the maximum extent practicable, any administrative burden such plan may place on Indian Tribes.\n##### (c) Definitions\nIn this section:\n**(1) Federal land management agency**\nThe term Federal land management agency means\u2014\n**(A)**\nthe Bureau of Land Management;\n**(B)**\nthe United States Fish and Wildlife Service;\n**(C)**\nthe National Park Service; and\n**(D)**\nthe Bureau of Indian Affairs.\n**(2) Indian Tribe**\nThe term Indian Tribe has the meaning given the term under section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 ).\n**(3) Permissive activity**\nThe term permissive activity includes\u2014\n**(A)**\nforest and grassland planning and management activities;\n**(B)**\nresearch and development activities;\n**(C)**\na restoration activity; and\n**(D)**\nrecreational services.\n**(4) Tribal Advisory Committee**\nThe term Tribal Advisory Committee means Secretary\u2019s Tribal Advisory Committee of the Department of the Interior (chartered on November 11, 2021).\n#### 3. Tribal co-management training\n##### (a) Training\nThe Secretary of the Interior shall ensure that each employee of the Department of the Interior who is involved in developing and carrying out a Tribal Co-Management Plan established under section 2 receives such training as the Secretary determines necessary to\u2014\n**(1)**\ntrain the employee to incorporate indigenous knowledge and practices into the execution of the plan;\n**(2)**\neducate the employee on the Tribal history of each area in which a project on which the employee is expect to work and which is approved to be carried out in accordance with the plan is located; and\n**(3)**\nprovide the employee with a general understanding of the trust relationship between the United States (including all agencies of the Federal Government) and Indian Tribes.\n##### (b) Consultation\nIn carrying out this section, the Secretary is authorized to consult with Indian Tribes.\n##### (c) Indian Tribe defined\nIn this section, the term Indian Tribe has the meaning given the term under section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 ).\n#### 4. Authority to enter into agreements with Indian Tribes and Tribal organizations to carry out certain Forest Service activities\n##### (a) Authority To enter into agreements with Indian Tribes and Tribal organizations\n**(1) Authority to enter into agreements**\n**(A) In general**\nSubject to subparagraph (B) and paragraph (3), the Secretary may enter into agreements with an Indian Tribe or Tribal organization for the performance of activities of the Forest Service described in paragraph (2).\n**(B) Minimum number of agreements**\nDuring the 4-year period beginning on the date of the enactment of this Act, the Secretary shall enter into at least 5 agreements under subparagraph (A).\n**(C) Agreement and contract authority**\nThe Secretary may carry out subparagraph (A)\u2014\n**(i)**\nthrough an agreement pursuant to this section;\n**(ii)**\nthrough a contract entered into under the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 et seq. ) in a substantially similar manner as a contract entered into pursuant to section 8703 of the Agriculture Improvement Act of 2018 ( 25 U.S.C. 3115b ); or\n**(iii)**\nthrough any other agreement authority provided to the Secretary under Federal law or regulations.\n**(2) Allowable activities**\n**(A) In general**\nAn activity described in this paragraph is any activity (including a permissive activity), service, or function (including the management decisions related to such activity, service, or function) of the Forest Service that\u2014\n**(i)**\nis carried out on National Forest System lands that the Secretary determines are in need of such activity (including restoration activity), service, or function;\n**(ii)**\nis consistent with each land management plan applicable to such National Forest System lands;\n**(iii)**\nis carried out on land that the Secretary, in consultation with each applicable Indian Tribe, identifies as being historically, culturally, or geographically related to such Indian Tribe; and\n**(iv)**\nis carried out in accordance with applicable laws, including environmental laws and regulations.\n**(B) Permissive activity**\nFor purposes of subparagraph (A), the term permissive activity includes\u2014\n**(i)**\nforest and grassland planning and management activities;\n**(ii)**\nresearch and development activities;\n**(iii)**\na restoration activity;\n**(iv)**\nactivities of the Heritage Program of the Forest Service; and\n**(v)**\nrecreational services.\n**(3) Limitations**\nThe Secretary may not enter into an agreement under paragraph (1)(A) that\u2014\n**(A)**\ndelegates any nondelegable function to an Indian Tribe or Tribal organization;\n**(B)**\nwould make an Indian Tribe or Tribal organization reliant on a State Government for the receipt of funds or other resources necessary to carry out any term of the agreement; or\n**(C)**\nprovides for the performance of an activity covered by a stewardship contract or other instrument such that the agreement would present a conflict with respect to National Forest System lands subject to the agreement.\n##### (b) Request for agreement\nTo request to enter into an agreement under subsection (a)(1)(A), an Indian Tribe or Tribal organization shall submit to the Secretary a proposal at such time and in such manner as the Secretary may require, including\u2014\n**(1)**\na description of each activity that the Indian Tribe or Tribal organization proposes to carry out under the agreement;\n**(2)**\nan identification of the National Forest System lands on which such activities are proposed to be carried out; and\n**(3)**\nany other information the Secretary may require.\n##### (c) Criteria for evaluating requested agreements\n**(1) Required considerations**\nBefore entering into an agreement under subsection (a)(1)(A), the Secretary shall consider\u2014\n**(A)**\nthe expected effects of the agreement on the interests of other Indian Tribes; and\n**(B)**\nwith respect to lands described in subsection (a)(2)(A), any valid existing rights and permits\u2014\n**(i)**\nof each Indian Tribe proposed to be subject to the agreement;\n**(ii)**\nof other Indian Tribes;\n**(iii)**\nof private parties; and\n**(iv)**\nof the Federal Government.\n**(2) Allowable evaluation and considerations**\nIn determining whether to enter into an agreement under subsection (a)(1)(A), the Secretary may\u2014\n**(A)**\nevaluate using a best-value basis the proposal submitted pursuant subsection (b) with respect to the agreement; and\n**(B)**\ngive special consideration to factors implicated by such proposal and related to the Indian Tribe proposed to be subject to the agreement, including\u2014\n**(i)**\nif applicable, the status of the Tribal organization that requested the agreement as a Tribal organization;\n**(ii)**\nthe historical, cultural, and traditional affiliation of the Indian Tribe with the land proposed to be subject to the agreement;\n**(iii)**\nthe features of the landscape of such land, including watersheds and vegetation types, that are expected to be affected if the proposal is carried out;\n**(iv)**\nwith respect to the coordination of activities, the working relationship, if any, between the Indian Tribe or Tribal organization that submitted the proposal and the Forest Service;\n**(v)**\naccess by members of the Indian Tribe proposed to be subject to the agreement to land proposed to be subject to the agreement; and\n**(vi)**\nthe indigenous knowledge and skills of the Indian Tribe and members of the Indian Tribe.\n##### (d) Notice of denial\nNot later than 90 days after the Secretary denies a request by an Indian Tribe or a Tribal organization pursuant to subsection (b), the Secretary shall issue to the Indian Tribe or Tribal organization a notice of denial that includes\u2014\n**(1)**\nan identification of each specific reason for the denial, including any criteria the Secretary considered pursuant to paragraphs (1) and (2) of subsection (c) that contributed to the denial;\n**(2)**\nan identification of the potential courses of action, if any, that the Indian Tribe or Tribal organization may take to overcome each such specific reason; and\n**(3)**\na proposed schedule for communication with the Indian Tribe or Tribal organization to provide technical assistance to the Indian Tribe or Tribal organization to overcome each such specific reason.\n##### (e) Payments to Indian Tribes or Tribal organizations\n**(1) In general**\nIn entering into an agreement under subsection (a)(1)(A)\u2014\n**(A)**\nthe Secretary may include terms and conditions with respect to payments to the Indian Tribe or Tribal organization party to the agreement for use carrying out the agreement; and\n**(B)**\nthe Indian Tribe or Tribal organization may elect to receive any such payments on an annual or semi-annual basis.\n**(2) Source of funds**\nThe Secretary shall\u2014\n**(A)**\nin the case of an activity to be carried out pursuant to an agreement under subsection (a)(1)(A), from the amounts appropriated to carry out such activity, use the unobligated amounts to make a payment under paragraph (1) with respect to such activity; or\n**(B)**\nif no such amounts are available, use the amounts made available pursuant to subsection (m) to make such a payment.\n**(3) Transfer authority**\nSubsections (a) through (l) of section 408 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5368 ) shall apply to the Secretary of Agriculture with respect to an agreement under subsection (a)(1)(A) in the same manner as such subsections apply to the Secretary of the Interior with respect to a funding agreement.\n**(4) Reduction of paperwork burden**\nIn carrying out this section, the Secretary shall, to the maximum extent practicable\u2014\n**(A)**\nreduce the reporting burden on Indian Tribes and Tribal organizations that receive funding pursuant to an agreement under this section, including by limiting report frequency, consolidating reporting requirements, and reducing required information; and\n**(B)**\nestablish such mechanisms as are necessary to protect Tribal data sovereignty.\n##### (f) Review and modification of agreement\n**(1) Periodic review**\nWith respect to an agreement under subsection (a)(1)(A) that is effective for a period of not fewer than 5 years, the Secretary shall, in the fifth year after the agreement takes effect and every 5 years thereafter during such period\u2014\n**(A)**\nreview the terms of the agreement with each Indian Tribe or Tribal organization party to the agreement; and\n**(B)**\noffer to modify any such terms or terminate the agreement, as the Secretary and each such Indian Tribe or the Tribal organization determines appropriate based on such review.\n**(2) Review due to natural disaster**\n**(A) Request to review**\nNot later than 90 days after a natural disaster occurs on National Forest System lands subject to an agreement under subsection (a)(1)(A), the Indian Tribe or Tribal organization party to the agreement may submit a request to the Secretary to\u2014\n**(i)**\nidentify any activities that could be carried out by the Indian Tribe or Tribal organization, in cooperation with the Forest Service and under the agreement, in response to the natural disaster; and\n**(ii)**\nreview the terms and conditions of the agreement to identify any modifications necessary to facilitate or authorize such activities.\n**(B) Review; modification**\nThe Secretary shall respond to a request under subparagraph (A) not later than 60 days after receiving such request.\n##### (g) Publication of activities\nNot later than 1 year after the date of the enactment of this Act and every 3 years thereafter, the Secretary, in consultation with Indian Tribes, shall publish in the Federal Register a non-exhaustive list describing the activities of the Forest Service that may be eligible for inclusion in an agreement under subsection (a)(1)(A).\n##### (h) Report\nNot later than 1 year after the date of the enactment of this Act and every 3 years thereafter, the Secretary shall submit to the relevant Congressional Committees a report containing a description of any progress or accomplishments made during the period covered by the report\u2014\n**(1)**\nwith respect to the activities of the Forest Service described in subsection (a)(2); and\n**(2)**\nattributable to an agreement under subsection (a)(1)(A).\n##### (i) Consultation\nIn carrying out this section, the Secretary shall consult with Indian Tribes to\u2014\n**(1)**\nensure that indigenous knowledge is\u2014\n**(A)**\nwhen requested by an applicable Indian Tribe or Tribal organization thereof, integrated into decision-making processes related to the activities carried out under this section; and\n**(B)**\nwhen appropriate, considered best available science; and\n**(2)**\nensure that appropriate safeguards exist to\u2014\n**(A)**\nprotect the integrity of indigenous knowledge; and\n**(B)**\nrespect the data sovereignty of Indian Tribes in accordance with Tribal law.\n##### (j) Federal Tort Claims Act applicability\nWhile engaged in carrying out an activity of the Forest Service pursuant to an agreement with an Indian Tribe or Tribal organization under subsection (a)(1)(A), an employee of such Indian Tribe or Tribal organization shall be considered to be an employee of the Forest Service for purposes of chapter 171 of title 28, United States Code.\n##### (k) FAR exemption\nThis Act, including any activity carried out pursuant to this section, is not subject to the requirements of the Federal Acquisition Regulation.\n##### (l) Effect\nNothing in this section\u2014\n**(1)**\nenlarges, establishes, or diminishes the current or future rights of any Indian Tribe;\n**(2)**\nreduces or supersedes any authority of an Indian Tribe to enter into agreements;\n**(3)**\nprovides exclusive use of any area within National Forest System lands;\n**(4)**\nlimits the Secretary from entering into a separate agreement with any other Indian Tribe, or Tribal organization thereof, with treaty rights or a recognized legal interest in National Forest System lands; or\n**(5)**\naffects the authority of the Secretary (as in effect on the date of the enactment of this Act) to, acting through the Chief of the Forest Service, enter into agreements to enable or accommodate Tribal activities on lands administered by the Forest Service, including the exercise of Tribal Treaty, reserved, retained, or other similar rights.\n##### (m) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $50,000,000 for the period of fiscal years 2026 through 2030, to remain available until expended.\n##### (n) Definitions\nIn this section:\n**(1) Agreement**\nThe term agreement includes a contract, compact, or any other similar mechanism.\n**(2) Indian Tribe**\nThe term Indian Tribe has the meaning given the term under section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 ).\n**(3) Indigenous knowledge**\nThe term indigenous knowledge includes, with respect to biological, physical, social, cultural, or spiritual phenomena, a body of observations, oral knowledge, written knowledge, innovations, practices, and beliefs developed by an Indian Tribe and members of the Indian Tribe through experience and interactions with the environment.\n**(4) National Forest System**\nThe term National Forest System has the meaning given such term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609 ).\n**(5) Natural disaster**\nThe term natural disaster includes\u2014\n**(A)**\na wildfire, hurricane, typhoon, tornado, excessive wind, hail, landslide, mudslide, drought, freeze, ice storm, snowstorm, blizzard, excessive moisture, flood, earthquake, extreme temperature event, insect or pathogen infestation, and volcanic eruption or emission; and\n**(B)**\nany other natural hazard that result in severe property damage, death, or injury, as determined by the Secretary.\n**(6) Relevant Congressional Committees**\nThe term relevant Congressional Committees means\u2014\n**(A)**\nthe Committees on Natural Resources and Agriculture of the House of Representatives; and\n**(B)**\nthe Committees on Indian Affairs, Energy and Natural Resources, and Agriculture, Nutrition, and Forestry of the Senate.\n**(7) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n**(8) Tribal organization**\nThe term Tribal organization means the recognized governing body of any Indian Tribe or any legally established organization of Indian Tribe members which is controlled, sanctioned, or chartered by such governing body or which is democratically elected by the adult members of the Indian community to be served by such organization and which includes the maximum participation of Indian Tribe members in all phases of its activities: Provided, That in any case where a contract is let or grant made to an organization to perform services benefitting more than one Indian Tribe, the approval of each such Indian Tribe shall be a prerequisite to the letting or making of such contract or grant.",
      "versionDate": "2025-05-15",
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
            "name": "Advisory bodies",
            "updateDate": "2025-07-11T18:30:24Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-11T18:30:19Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-07-11T18:29:55Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-07-11T18:29:35Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-11T18:30:12Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-07-11T18:29:17Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-07-11T18:29:45Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-07-11T18:29:24Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2025-07-11T18:30:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-06-18T15:11:44Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3444ih.xml"
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
      "title": "Tribal Self-Determination and Co-Management in Forestry Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tribal Self-Determination and Co-Management in Forestry Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct Federal land management agencies of the Department of the Interior to establish Tribal Co-Management Plans and to authorize the Secretary of Agriculture to enter into agreements with Indian Tribes and Tribal organizations for the performance of certain activities of the Forest Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:33:21Z"
    }
  ]
}
```
