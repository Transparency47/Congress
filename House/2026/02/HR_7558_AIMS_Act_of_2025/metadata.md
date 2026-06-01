# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7558?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7558
- Title: AIMS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 7558
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-05-07T02:41:50Z
- Update date including text: 2026-05-07T02:41:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7558",
    "number": "7558",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001183",
        "district": "1",
        "firstName": "David",
        "fullName": "Rep. Schweikert, David [R-AZ-1]",
        "lastName": "Schweikert",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "AIMS Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-07T02:41:50Z",
    "updateDateIncludingText": "2026-05-07T02:41:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-12T14:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7558ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7558\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Schweikert introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Defense and the Secretary of Veterans Affairs to jointly adopt and use interoperable image-sharing software technology for the purpose of sharing medical images and related data at medical facilities of the Department of Defense and Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Achieving Interoperability of Medical Systems Act of 2025 or the AIMS Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSection 1635 of the National Defense Authorization Act for Fiscal Year 2008 ( Public Law 110\u2013181 ; 10 U.S.C. 1071 note) directed the Secretary of Defense and the Secretary of Veterans Affairs to jointly\u2014\n**(A)**\ndevelop and implement electronic record systems that allow full interoperability of personal health care information between the Department of Defense and the Department of Veterans Affairs; and\n**(B)**\naccelerate the exchange of such information between the two departments.\n**(2)**\nSuch section established the Department of Defense-Department of Veterans Affairs Interagency Program Office (with a Director and Deputy Director) for such purposes and authorized the Secretaries to carry out pilot projects to assess the feasibility and advisability of various technological approaches to the development of the record systems.\n**(3)**\nSuch section also requires\u2014\n**(A)**\nthe Director of the Interagency Program Office to submit to the Secretaries and to Congress annual reports on the activities of the Office;\n**(B)**\nthe Secretaries to make such reports available to the public; and\n**(C)**\nthe Comptroller General of the United States to conduct semiannual assessments of the progress of the Secretaries in carrying out the requirements of such section.\n#### 3. Department of Defense and Department of Veterans Affairs interoperability of medical images and related data\n##### (a) In general\nThe Secretary of Veterans Affairs and the Secretary of Defense shall jointly adopt and use interoperable image-sharing software technology\u2014\n**(1)**\naccessible by facilities of the military health service, as well as the GENESIS platform of the military health service and the Federal Electronic Health Record platform of the Department of Veterans Affairs; and\n**(2)**\nat each Department of Veterans Affairs and Department of Defense medical facility.\n##### (b) Scope\nThe technology adopted and used under subsection (a) shall provide for interoperability between all of the following:\n**(1)**\nMilitary medical centers included in the Military Health System.\n**(2)**\nDepartment of Veterans Affairs medical facilities and clinics.\n**(3)**\nNon-Department providers that have entered into agreements with the Secretary of Veterans Affairs under section 1703 of title 38, United States Code.\n##### (c) Plan\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense and the Secretary of Veterans Affairs shall provide to the Committees on Armed Services and the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a briefing and submit to such committees a report on the plan of the Secretaries, and an associated timeline, for achieving the full interoperability of medical images and related data between the Department of Defense and Department of Veterans Affairs in accordance with subsection (a). The plan shall include each of the following:\n**(1)**\nThe expansion of the services provided pursuant to contracts entered into between the Secretary of Defense, the Secretary of Veterans Affairs, and application-based vendors that meet interoperability standards.\n**(2)**\nAn assessment and comparison of the baseline medical image interoperability that exists, as of the date of the enactment of this Act, between the Department of Defense and the Department of Veterans Affairs and external partners of such departments, including\u2014\n**(A)**\nnon-Department of Veterans Affairs imaging providers described in section 1703(c) of title 38, United States Code; and\n**(B)**\nimagining providers who are described in section 199.6 of title 32 of the Code of Federal Regulations, or any successor regulation.\n**(3)**\nAn identification of one or more licensed interoperability software technology solutions of choice that\u2014\n**(A)**\nis shared by hospitals and health care providers to benefit patients before and after discharge from provider care and that is accessible to current and future providers, in compliance with applicable accessibility requirements, including mobile user interface, as established in the Information and Communication Technology and Software portions of the Revised 508 Standards under part 1194 of title 36 of the Code of Federal Regulations, or any successor regulation, and in adherence with the Web Content Accessibility Guidelines 2.1AA, as established by the World Wide Web Consortium and in effect on the date of the enactment of this Act;\n**(B)**\nenables the electronic medical records system of a hospital, or in the case of a Department of Veterans Affairs facility, the Federal Electronic Health Record of the Department, to interface with interoperability technology and other electronic medical records systems and providers to promote mobile connectivity between hospital systems and facilitate increased communication between hospital staff and providers that use different or distinctive online and mobile platforms and information systems when treating acute patients;\n**(C)**\ncaptures and forwards clinical data, including laboratory results and images, provider notes, historical clinical conditions, procedures, medications, cardiology testing results, and vital signs, and provides synchronous patient clinical data to health care providers regardless of geographic location;\n**(D)**\nprovides a synchronous data exchange that is not batched or delayed, at the point the clinical data is captured and available in the electronic record system of a hospital;\n**(E)**\nis capable of providing proactive alerts to health care providers on their smartphones or a smart device;\n**(F)**\nallows both synchronous and asynchronous communication using a native smartphone application;\n**(G)**\nis mobile, can be used on multiple electronic devices, and includes the industry standard 39 built-in application for the two most popular operating systems and a built-in application available to all users;\n**(H)**\nas patient-centric communication and is tracked with date and time stamping;\n**(I)**\nprovides interoperability to include imaging-related workflows of image exchange, sharing, and collaboration;\n**(J)**\nprovides enterprise-wide deployment that is comparable to the size and complexity of the largest integrated health care system in the country;\n**(K)**\nallows a patient to manage their own health using a mobile application in alignment with wearable technology devices or the function referred to as the Share My Health Data available through the Veterans Health Administration;\n**(L)**\nadheres to integration standards for software applications to connect to an electronic health record system, or in the case of a Department of Veterans Affairs medical facility or a Military Health System facility, use a Federal Electronic Health Record system, as established by the Office of the National Coordinator for Health Information Technology of the Department of Health and Human Services, including\u2014\n**(i)**\nSubstitutable Medical Applications, Reusable Technologies on Fast Healthcare Interoperability Resources, known as SMART on FHIR , which allows third-party applications to integrate directly with electronic health records and patient portals;\n**(ii)**\nopen authorization protocol 2.0 (OAuth2) for session authentication, which bolsters security and patient safety by only allowing authorized users with validated access to view, share, and import images and related data; and\n**(iii)**\nDigital Imaging and Communications in Medicine, which is the regulated standard for medical images; and\n**(M)**\nis cost-effective with a high return on investment that is supported by the use of artificial intelligence in the image sharing workflow.\n##### (d) Requirements for plan\nIn developing the plan required under subsection (b), the Secretaries shall ensure that\u2014\n**(1)**\nthe software used for interoperable medical images and related data of the Departments is designed to\u2014\n**(A)**\nimprove health care delivery and quality by addressing the increased costs, delays, and patient burden of repeat images caused by the couriering of compact discs and DVD\u2013ROMs as the primary mechanism for sharing patients\u2019 medical images in the continuum of care;\n**(B)**\nthe plan includes the development, by not later than two years after the date of the enactment of this Act, of a robust data storage platform capable of storing health data from the Department of Veterans Affairs, the military health service, and health information exchanges used by non-Department providers that have entered into agreements with the Secretary of Veterans Affairs under section 1703 of title 38, United States Code;\n**(C)**\nprovide patient-centered care by facilitating faster diagnoses, enabling more informed decision-making and promoting better communication;\n**(D)**\nsupport more efficient use of the time of clinical and support staff and improve retention by helping to prevent burnout; and\n**(E)**\npromote the effective use of shared services between the Departments, including joint facilities and military treatment facilities that provide clinic space for the Department of Veterans Affairs, and in coordination with non-Department providers that have entered into agreements with the Secretary of Veterans Affairs under section 1703 of title 38, United States Code; and\n**(2)**\nthe plan includes an implementation timeline and associated milestones, and an identification of the projected total cost.\n##### (e) Reports\nNot later than six months after the date of the submission of the report required under subsection (b), and annually months thereafter, the Secretary of Defense and the Secretary of Veterans Affairs shall jointly provide a briefing and submit to the Committees on Armed Services and the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate on\u2014\n**(1)**\nany updates to the plan included in the report required under subsection (b); and\n**(2)**\nmetrics and quantified cost and time savings associated with using an interoperable software solution in health care that complies with the health insurance portability and accountability act privacy standards under part 160 and part 164, subpart of title 4 of the Code of Federal Regulations, as in effect on the date of the enactment of this Act.\n##### (f) Definitions\nIn this section:\n**(1)**\nThe term GENESIS means the electronic health record system known as MHS GENESIS that is used by the military health service.\n**(2)**\nThe term military treatment facility has the meaning given such term in section 1073c of title 10, United States Code.\n**(3)**\nThe term electronic health record means an electronic version of a patient's medical history, that\u2014\n**(A)**\nis maintained by the provider over time, and may include all of the key administrative clinical data relevant to that person's care under a particular provider, including demographics, progress notes, problems, medications, vital signs, past medical history, immunizations, laboratory data and radiology reports;\n**(B)**\nautomates access to information and has the potential to streamline the clinician's workflow; and\n**(C)**\nhas the ability to support other care-related activities directly or indirectly through various interfaces, including evidence-based decision support, quality management, and outcomes reporting.",
      "versionDate": "2026-02-12",
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
        "updateDate": "2026-05-07T02:41:50Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7558ih.xml"
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
      "title": "AIMS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T05:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AIMS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T05:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Achieving Interoperability of Medical Systems Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T05:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense and the Secretary of Veterans Affairs to jointly adopt and use interoperable image-sharing software technology for the purpose of sharing medical images and related data at medical facilities of the Department of Defense and Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T05:03:57Z"
    }
  ]
}
```
