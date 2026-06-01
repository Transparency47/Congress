# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6721?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6721
- Title: MAP for Care Act
- Congress: 119
- Bill type: HR
- Bill number: 6721
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-04-21T17:50:00Z
- Update date including text: 2026-04-21T17:50:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-15 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6721",
    "number": "6721",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "MAP for Care Act",
    "type": "HR",
    "updateDate": "2026-04-21T17:50:00Z",
    "updateDateIncludingText": "2026-04-21T17:50:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-15T17:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6721ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6721\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Mr. Murphy (for himself and Mr. Thompson of California ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to encourage Medicare beneficiaries to voluntarily adopt advance directives guiding the medical care they receive.\n#### 1. Short title\nThis Act may be cited as the Medicare Advance Planning for Care Act or the MAP for Care Act .\n#### 2. Medicare Advance Directive Certification Program\nPart B of title XVIII of the Social Security Act ( 42 U.S.C. 1395j et seq. ) is amended by adding at the end the following new section:\n1849. Medicare Advance Directive Certification Program (a) In general (1) Establishment of Program The Secretary shall establish and implement an Advance Directive Certification Program (in this section referred to as the Program ) under which the Secretary shall encourage eligible beneficiaries to adopt and maintain certified advance directives to guide the delivery of health care to such beneficiaries. The Secretary shall implement the Program not later than 5 years after the date of enactment of this section. (2) Definitions In this section: (A) Certified advance directive The term certified advance directive means an electronically stored written instruction by an eligible beneficiary, such as a living will or durable power of attorney for health care, recognized under State law (whether statutory or as recognized by the courts of the State) and relating to the provision of such care when the individual is incapacitated that\u2014 (i) provides instructions that outline the kind of medical treatments and care that such beneficiary would want or not want under particular conditions, and may also include the identification of a health care proxy or legal representative to make medical treatment decisions for the beneficiary if the beneficiary becomes unable to make or communicate those decisions on their own; and (ii) is offered by an entity that has received accreditation from the Secretary under subsection (c). (B) Eligible beneficiary The term eligible beneficiary means an individual entitled to, or enrolled for benefits, under part A or enrolled for benefits under this part. (C) Program participant The term Program participant means an eligible beneficiary who is enrolled in the Program. (3) Voluntary participation An eligible beneficiary who has registered a certified advance directive with a advance directive vendor accredited under subsection (c) may disenroll and terminate such directive at any time. (4) Best practices In establishing and implementing the Program, the Secretary shall consider best practices\u2014 (A) within existing advance directive registry technologies, programs, and systems, including web-based or cloud-based advance directive technologies\u2014 (i) which may utilize time and date stamps, video, or other innovative measures to protect the authenticity, improve the quality of, and enhance the security of such directives; and (ii) which may utilize secure email and messaging technologies and nationally recognized health care information technology standards to improve the accessibility and interoperability of such directives; and (B) for educating beneficiaries on ways to\u2014 (i) communicate their authenticated wishes to applicable family members, legal representatives, and providers or health care proxies, including through the use of email or other mail formats; and (ii) access certified advance directives, including through the use of mobile devices. (5) State law The provisions of this section shall not preempt any State or local law requirement governing advance directives. (6) Display of statutory and alternative advance directive forms Under the Program, the Secretary shall provide, on the Internet website of the Centers for Medicare & Medicaid Services, links to statutory advance directive forms (as described in subsection (d)(1)(C)), alternative advance directive forms (as described in subsection (d)(1)(D)), and a State-by-State index to such forms to allow a Program participant to create, adopt, modify, and terminate a certified advance directive with any content permitted or required under this section, and in any form authorized by a State. (b) Enrollment in the Program and registration of advance directives (1) Required information In addition to such other information as the Secretary determines is appropriate, a Program participant seeking to register a certified advance directive under the Program shall indicate where the advance directive is maintained or how it may be accessed. (2) Notification regarding Program During the annual, coordinated election period under section 1851(e)(3), the Secretary shall notify each eligible beneficiary of the Program. (3) Privacy and security (A) In general The Secretary shall ensure that all aspects of the enrollment and registration system comply with the Federal regulations (concerning the privacy and security of individually identifiable health information) promulgated under the Health Insurance Portability and Accountability Act of 1996 subject to the access authorized under subsection (c)(2)(E) and in accordance with subsection (c)(2)(F). (B) Access The Secretary shall utilize standardized data protections and privacy standards, including the Federal regulations described in subparagraph (A), to ensure that the registration record of a Program participant can only be accessed by\u2014 (i) the Program participant, through the process established under subsection (c)(2)(B); (ii) those authorized to access the certified advance directive under subsection (c)(2)(E); and (iii) providers of services and suppliers participating under this title who furnish items or services to the Program participant, through a process established by the Secretary. (c) Accreditation (1) In general (A) Accreditation by the Secretary Under the Program, the Secretary shall\u2014 (i) accredit advance directive vendors and other entities providing advance directives that meet the accreditation criteria established under paragraph (2) and any other criteria determined appropriate by the Secretary; and (ii) establish a process whereby advance directive vendors and other entities providing advance directives may obtain accreditation under this subsection. (B) Accreditation by advance directive accreditation organization The Secretary may contract with an advance directive accreditation organization to accredit advance directive vendors and other entities under subparagraph (A)(i). (2) Accreditation criteria The Secretary, in consultation with the Comptroller General of the United States, shall establish accreditation criteria for advance directive vendors and other entities providing advance directives to be certified under the Program. Such criteria shall consist of each of the following: (A) Certified advance directives The advance directive vendor or other entity shall agree to offer certified advance directives to eligible beneficiaries. (B) Procedures for enrollment (i) In general The advance directive vendor or other entity shall establish procedures that\u2014 (I) allow for a Program participant to\u2014 (aa) enroll in and disenroll from the Program; and (bb) register or update a certified advance directive adopted by the participant; and (II) ensure that a Program participant is able to\u2014 (aa) create, adopt, modify, update, amend, or terminate a certified advance directive in a timely and secure manner; (bb) update previously registered information; and (cc) indicate that a previously registered certified advance directive has been terminated. (ii) Online enrollment and registration The procedures established pursuant to clause (i) shall ensure that such enrollment and registration is available through an online process, or other means determined appropriate by the advance directive vendor or other entity. (C) Quality review (i) In general For purposes of determining compliance with the requirements of this section, the advance directive vendor or other entity shall comply with an annual quality review to be conducted by the Secretary. (ii) Enforcement If the Secretary determines that an advance directive vendor or other entity is not in compliance with the requirements of this section, the Secretary shall remove any certified advance directive of such advance directive vendor or other entity from the Internet website of the Centers for Medicare & Medicaid Services. (D) Use of statutory and alternative advance directive forms The advance directive vendor or other entity shall allow a Program participant to\u2014 (i) access, complete, modify, and adopt any advance directive forms described in subparagraphs (C) and (D) of subsection (d)(1); and (ii) search for such forms by State. (E) Access The advance directive vendor or other entity shall\u2014 (i) provide near real-time online access to the certified advance directive of a Program participant for purposes of viewing and sharing such advance directive, including communicating the certified advance directive and the Program participant\u2019s authenticated wishes using nationally recognized standards for securely transferring sensitive data specified by the Secretary to\u2014 (I) the Program participant; (II) any family member, legal representative, or health care proxy legally designated by the participant; and (III) a provider of services or supplier that furnishes items or services to the participant; and (ii) at the request of the Program participant or any family member, legal representative, or health care proxy legally designated by the Program participant, provide a hard copy of the certified advance directive of the Program participant to a provider of services or supplier. (F) Privacy protections (i) In general The advance directive vendor or other entity shall comply with the Federal regulations (concerning the privacy of individually identifiable health information) promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996, subject to the access authorized under subparagraph (E). (ii) Access Such vendor or entity shall comply with standardized data protections and privacy standards, including the Federal Regulations described in clause (i), to ensure that the content of a Program participant\u2019s certified advance directive is owned and maintained by the participant and can only be accessed by those authorized to access the advance directive under subparagraph (E). (G) Security and testing The advance directive vendor or other entity shall certify that\u2014 (i) all data management and data transfer elements involved in adopting, maintaining, and accessing a certified advance directive of a Program participant\u2014 (I) have successfully passed rigorous independent testing regarding standards of timeliness, accuracy, and efficiency; and (II) meet widely accepted industry security standards (as determined by the Secretary); and (ii) the system that provides access to a certified advance directive of a Program participant has passed real-time tests simulating a realistic volume of Program participants, their family members, legal representatives, and legally designated health care proxies, providers of services, and suppliers accessing such directives simultaneously. (H) Beneficiary surveys (i) In general The advance directive vendor or other entity shall administer an annual survey of Program participants on the information described in clause (ii) and submit the results of such survey to the Secretary. (ii) Information The information described in this clause, with respect to a Program participant and a certified advance directive of such participant, is the following: (I) Whether the participant had to pay any third party for the creation, storage, or retrieval of the certified advance directive. (II) Whether the participant had a health care encounter or emergency that required the location, access, retrieval, or consultation of the certified advance directive and if so, whether the certified advance directive was accessible online and in near real-time, as required under this section. (III) Whether the certified advance directive was sufficiently clear and actionable. (IV) Whether medical personnel followed the certified advance directive. (I) Process for complying with State law The advance directive vendor or other entity shall enable a Program participant using their services to complete a certified advance directive that fully complies with the law governing advance directives of the applicable State. (J) Access in cases of dispute over treatment (i) Special access The advance directive vendor or other entity shall establish a process whereby, with respect to a Program participant, an interested individual described in clause (ii) may obtain access to the certified advance directive of the Program participant for the purposes of viewing and sharing such advance directive when\u2014 (I) the provisions of the certified advance directive have come into force under the law of the applicable State because the Program participant has become incapable of making health care decisions on their own or under other circumstances provided under State law; and (II) at least 1 person described in clause (ii) is questioning or disputing the provision, withholding, or withdrawal of medical treatment, food, or fluids with respect to the Program participant. (ii) Interested individuals (I) In general An interested individual described in this clause, with respect to a Program participant, is\u2014 (aa) any individual who is a member of any class of persons who, under the law of the applicable State, would potentially be eligible to serve as a health care decision maker for the Program participant if an advance directive had not been executed, regardless of whether another individual would have higher priority for such eligibility; or (bb) if the law of the applicable State does not designate a person or class of persons described in item (aa), any individual related within the third degree of consanguinity or affinity to the Program participant identified by the Program participant in the certified advance directive. (II) Periodic update In the case that the law of the applicable State does not designate a person or class of persons described in subclause (I)(aa) and the Program participant has identified in a certified advance directive an individual within the third degree of consanguinity or affinity of such participant, the advance directive vendor or other entity shall annually during the annual, coordinated election period under section 1851(e)(3) prompt the Program participant to update such individual. (d) Education and outreach (1) In general The Secretary shall\u2014 (A) include a statement described in paragraph (3) in the notice described in section 1804(a) and provide for the inclusion of such statement on the Internet website of the Centers for Medicare & Medicaid Services; (B) communicate the benefits of electronic advance directives services, as they become available; (C) provide for the inclusion, under the heading Statutory Advance Directive Forms , of any relevant forms, whether mandatory or optional, specified in the statutes or regulations of States to be displayed on a such website; (D) provide for the inclusion, under the heading Alternative Advance Directive Forms , on such website, and in accordance with paragraph (2)\u2014 (i) of other advance directive forms submitted to the Secretary by individuals and groups in an electronic format specified by the Secretary for which the submitting entity includes, for each form submitted, an opinion by an attorney licensed to practice in the relevant State demonstrating that the submitted form complies with the law of that State; and (ii) of the following disclaimer, which shall be prominently posted on the website: This website includes for your consideration alternative advance directive forms submitted by individuals or groups reflecting different perspectives on advance health care decisions which you may wish to review before completing your own advance directive. ; and (E) provide for the inclusion of a user-friendly index on the website by State and, in the case of the Alternative Advance Directive Forms , by the name of the individual or group who provided each alternative advance directive, so that a user may readily access those statutory and alternative forms. (2) Alternative advance directive forms (A) In general For purposes of paragraph (1)(D), the following shall apply: (i) Not later than 60 days after receiving an alternative advance directive form submitted under such paragraph, the Secretary shall either post the submitted form on the Internet website of the Centers for Medicare & Medicaid Services or provide to the submitting entity an explanation of the basis for the Secretary\u2019s determination that the submitted form does not comply with relevant State or Federal law, which determination shall be subject to judicial review under section 702 of title 5 of the United States Code. (ii) The Secretary shall either remove or refuse to post any submitted form if provided with an official determination by the attorney general of the applicable State that the form is not in compliance with State law, subject to applicable State law described in subparagraph (B). (B) State law described For purposes of subparagraph (A), State law described in this subparagraph is\u2014 (i) a ruling by a court of the applicable State, or by a Federal court applying that State\u2019s law, subject to subsequent rulings by a court or courts with authority to supercede that ruling; or (ii) a statute or regulation of the applicable State that provides for a specific procedure for officially determining whether particular advance directive forms comply with State law. (3) Statement For purposes of paragraph (1)(A), the statement described in this paragraph is a statement of the reasons why beneficiaries may want to consider advance directives, a suggestion for the beneficiary to carefully consider decisions regarding advance directives, and references to resources about advance directives. (e) Advance directive information in Medicare enrollment forms After the Secretary implements the Program, the Secretary shall include on each application for enrollment of an individual in part A, this part, or part C a link to an Internet website with resources to assist in completing an advance directive. .",
      "versionDate": "2025-12-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-15",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3473",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MAP for Care Act",
      "type": "S"
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
        "updateDate": "2026-04-21T17:49:59Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6721ih.xml"
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
      "title": "MAP for Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MAP for Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicare Advance Planning for Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to encourage Medicare beneficiaries to voluntarily adopt advance directives guiding the medical care they receive.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T05:33:36Z"
    }
  ]
}
```
