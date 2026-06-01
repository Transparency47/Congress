# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4062?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4062
- Title: Next Generation 9–1–1 Act
- Congress: 119
- Bill type: S
- Bill number: 4062
- Origin chamber: Senate
- Introduced date: 2026-03-11
- Update date: 2026-04-13T13:11:13Z
- Update date including text: 2026-04-13T13:11:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-11: Introduced in Senate
- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-11: Introduced in Senate

## Actions

- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-11",
    "latestAction": {
      "actionDate": "2026-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4062",
    "number": "4062",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Next Generation 9\u20131\u20131 Act",
    "type": "S",
    "updateDate": "2026-04-13T13:11:13Z",
    "updateDateIncludingText": "2026-04-13T13:11:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-11",
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
          "date": "2026-03-11T20:09:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4062is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4062\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2026 Ms. Klobuchar (for herself, Mr. Budd , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the National Telecommunications and Information Administration Organization Act to provide for further deployment and coordination of Next Generation 9\u20131\u20131, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Next Generation 9\u20131\u20131 Act .\n#### 2. Further deployment and coordination of Next Generation 9\u20131\u20131\nPart C of the National Telecommunications and Information Administration Organization Act is amended by adding at the end the following:\n159. Coordination of Next Generation 9\u20131\u20131 implementation (a) Duties of Assistant Secretary with respect to Next Generation 9\u20131\u20131 (1) In general The Assistant Secretary, after consulting with the Administrator, shall\u2014 (A) take actions, in coordination with State points of contact described under subsection (c)(3)(A)(ii) as applicable, to improve coordination and communication with respect to the implementation of Next Generation 9\u20131\u20131; (B) develop, collect, and disseminate information concerning the practices, procedures, and technology used in the implementation of Next Generation 9\u20131\u20131; (C) advise and assist eligible entities in the preparation of implementation plans required under subsection (c)(3)(A)(iii); (D) provide technical assistance to eligible entities provided a grant under subsection (c) in support of efforts to explore efficiencies related to Next Generation 9\u20131\u20131; (E) review and approve or disapprove applications for grants under subsection (c); and (F) oversee the use of funds provided by such grants in fulfilling such implementation plans. (2) Annual reports Not later than October 1, 2027, and each year thereafter until funds made available to make grants under subsection (c) are no longer available to be expended, the Assistant Secretary shall submit to Congress a report on the activities conducted by the Assistant Secretary under paragraph (1) in the year preceding the submission of the report. (3) Assistance The Assistant Secretary may seek the assistance of the Administrator in carrying out the duties described in subparagraphs (A) through (D) of paragraph (1) as the Assistant Secretary determines necessary. (b) Additional duties (1) Management plan (A) Development The Assistant Secretary, after consulting with the Administrator, shall develop a management plan for the grant program established under this section, including by developing\u2014 (i) plans related to the organizational structure of such program; and (ii) funding profiles for each fiscal year of the duration of such program. (B) Submission to congress Not later than 180 days after the date of enactment of this section, the Assistant Secretary shall\u2014 (i) submit the management plan developed under subparagraph (A) to\u2014 (I) the Committees on Commerce, Science, and Transportation and Appropriations of the Senate; and (II) the Committees on Energy and Commerce and Appropriations of the House of Representatives; (ii) publish the management plan on the website of the National Telecommunications and Information Administration; and (iii) provide the management plan to the Administrator for the purpose of publishing the management plan on the website of the National Highway Traffic Safety Administration. (2) Modification of plan (A) Modification The Assistant Secretary, after consulting with the Administrator, may modify the management plan developed under paragraph (1)(A). (B) Submission Not later than 90 days after the plan is modified under subparagraph (A), the Assistant Secretary shall\u2014 (i) submit the modified plan to\u2014 (I) the Committees on Commerce, Science, and Transportation and Appropriations of the Senate; and (II) the Committees on Energy and Commerce and Appropriations of the House of Representatives; (ii) publish the modified plan on the website of the National Telecommunications and Information Administration; and (iii) provide the modified plan to the Administrator for the purpose of publishing the modified plan on the website of the National Highway Traffic Safety Administration. (c) Next generation 9\u20131\u20131 implementation grants (1) Grants The Assistant Secretary shall provide grants to eligible entities for\u2014 (A) implementing Next Generation 9\u20131\u20131; (B) maintaining Next Generation 9\u20131\u20131; (C) training directly related to implementing, maintaining, and operating Next Generation 9\u20131\u20131 if the cost related to the training does not exceed\u2014 (i) 3 percent of the total grant award for eligible entities that are not Tribes; and (ii) 5 percent of the total grant award for eligible entities that are Tribes; (D) public outreach and education on how the public can best use Next Generation 9\u20131\u20131 and the capabilities and usefulness of Next Generation 9\u20131\u20131; (E) administrative costs associated with planning of Next Generation 9\u20131\u20131, including any cost related to planning for and preparing an application and related materials as required by this subsection, if\u2014 (i) the cost is fully documented in materials submitted to the Assistant Secretary; and (ii) the cost is reasonable, necessary, and does not exceed\u2014 (I) 1 percent of the total grant award for eligible entities that are not Tribes; and (II) 2 percent of the total grant award for eligible entities that are Tribes; and (F) costs associated with implementing cybersecurity measures at emergency communications centers or with respect to Next Generation 9\u20131\u20131. (2) Application In providing grants under paragraph (1), the Assistant Secretary, after consulting with the Administrator, shall require an eligible entity to submit to the Assistant Secretary an application, at the time and in the manner determined by the Assistant Secretary, and containing the certification required by paragraph (3). (3) Coordination required Each eligible entity shall include in the application required by paragraph (2) a certification that\u2014 (A) in the case of an eligible entity that is a State, the entity\u2014 (i) has coordinated the application with the emergency communications centers located within the jurisdiction of the entity; (ii) has designated a single officer or governmental body to serve as the State point of contact to coordinate the implementation of Next Generation 9\u20131\u20131 for that State, except that such designation need not vest such officer or governmental body with direct legal authority to implement Next Generation 9\u20131\u20131 or to manage emergency communications operations; and (iii) has developed and submitted a plan for the coordination and implementation of Next Generation 9\u20131\u20131 that\u2014 (I) ensures interoperability by requiring the use of commonly accepted standards; (II) ensures reliability; (III) enables emergency communications centers to process, analyze, and store multimedia, data, and other information; (IV) incorporates cybersecurity tools, including intrusion detection and prevention measures; (V) includes strategies for coordinating cybersecurity information sharing between Federal, State, Tribal, and local government partners; (VI) uses open and competitive request for proposal processes, including through shared government procurement vehicles, for deployment of Next Generation 9\u20131\u20131; (VII) documents how input was received and accounted for from relevant rural and urban emergency communications centers, regional authorities, local authorities, and Tribal authorities; (VIII) includes a governance body or bodies, either by creation of new, or use of existing, body or bodies, for the development and deployment of Next Generation 9\u20131\u20131 that\u2014 (aa) ensures full notice and opportunity for participation by relevant stakeholders; and (bb) consults and coordinates with the State point of contact required by clause (ii); (IX) creates efficiencies related to Next Generation 9\u20131\u20131 functions, including cybersecurity and the virtualization and sharing of infrastructure, equipment, and services; and (X) utilizes an effective, competitive approach to establishing authentication, credentialing, secure connections, and access in deploying Next Generation 9\u20131\u20131, including by\u2014 (aa) requiring certificate authorities to be capable of cross-certification with other authorities; (bb) avoiding risk of a single point of failure or vulnerability; and (cc) adhering to Federal agency best practices such as those promulgated by the National Institute of Standards and Technology; and (B) in the case of an eligible entity that is a Tribe, the Tribe has complied with clauses (i) and (iii) of subparagraph (A). (4) Criteria (A) In general Not later than 1 year after the date of enactment of this section, the Assistant Secretary, after consulting with the Administrator, shall issue rules, after providing the public with notice and an opportunity to comment, prescribing the criteria for selecting eligible entities for grants under this subsection. (B) Requirements The criteria described in subparagraph (A) shall\u2014 (i) include performance requirements and a schedule for completion of any project to be financed by a grant under this subsection; and (ii) specifically permit regional or multi-State applications for funds. (C) Updates The Assistant Secretary shall update the rules issued under subparagraph (A) as necessary. (5) Grant certifications Each eligible entity shall certify to the Assistant Secretary at the time of application for a grant under this subsection, and each eligible entity that receives such a grant shall certify to the Assistant Secretary annually thereafter during any period of time the funds from the grant are available to the eligible entity, that\u2014 (A) beginning on the date that is 180 days before the date on which the application is filed, no portion of any 9\u20131\u20131 fee or charge imposed by the eligible entity (or in the case that the eligible entity is not a State or Tribe, any State or taxing jurisdiction within which the eligible entity will carry out, or is carrying out, activities using grant funds) are obligated or expended for a purpose or function not designated under the rules issued pursuant to section 6(f)(3) of the Wireless Communications and Public Safety Act of 1999 ( 47 U.S.C. 615a\u20131(f)(3) ) (as such rules are in effect on the date on which the eligible entity makes the certification) as acceptable; (B) any funds received by the eligible entity will be used, consistent with paragraph (1), to support the deployment of Next Generation 9\u20131\u20131 that ensures reliability and interoperability, by requiring the use of commonly accepted standards; (C) the eligible entity (or in the case that the eligible entity is not a State or Tribe, any State or taxing jurisdiction within which the eligible entity will carry out or is carrying out activities using grant funds) has established, or has committed to establish not later than 3 years following the date on which the grant funds are distributed to the eligible entity\u2014 (i) a sustainable funding mechanism for Next Generation 9\u20131\u20131; and (ii) effective cybersecurity resources for Next Generation 9\u20131\u20131; (D) the eligible entity will promote interoperability between emergency communications centers deploying Next Generation 9\u20131\u20131 and emergency response providers, including users of the nationwide public safety broadband network; (E) the eligible entity has or will take steps to coordinate with adjoining States and Tribes to establish and maintain Next Generation 9\u20131\u20131; and (F) the eligible entity has developed a plan for public outreach and education on how the public can best use Next Generation 9\u20131\u20131 and on the capabilities and usefulness of Next Generation 9\u20131\u20131. (6) Condition of grant Each eligible entity shall agree, as a condition of receipt of a grant under this subsection, that if any State or taxing jurisdiction within which the eligible entity will carry out activities using grant funds fails to comply with a certification required under paragraph (5), during any period of time during which the funds from the grant are available to the eligible entity, all of the funds from such grant shall be returned to the Assistant Secretary. (7) Penalty for providing false information Any eligible entity that provides a certification under paragraph (5) knowing that the information provided in the certification was false shall\u2014 (A) not be eligible to receive the grant under this subsection; (B) return any grant awarded under this subsection; and (C) not be eligible to receive any subsequent grants under this subsection. (8) Prohibition Grant funds provided under this subsection may not be used\u2014 (A) to support any activity of the First Responder Network Authority; or (B) to make any payments to a person who has been, for reasons of national security, prohibited by any entity of the Federal Government from bidding on a contract, participating in an auction, or receiving a grant. (d) Definitions In this section and sections 160 and 161: (1) 9\u20131\u20131 fee or charge The term 9\u20131\u20131 fee or charge has the meaning given the term in section 6(f)(3)(D) of the Wireless Communications and Public Safety Act of 1999 ( 47 U.S.C. 615a\u20131(f)(3)(D) ). (2) 9\u20131\u20131 request for emergency assistance The term 9\u20131\u20131 request for emergency assistance means a communication, such as voice, text, picture, multimedia, or any other type of data, that is sent to an emergency communications center for the purpose of requesting emergency assistance. (3) Administrator The term Administrator means the Administrator of the National Highway Traffic Safety Administration. (4) Commonly accepted standards The term commonly accepted standards means the technical standards followed by the communications industry for network, device, and Internet Protocol connectivity that\u2014 (A) enable interoperability; and (B) are\u2014 (i) developed and approved by a standards development organization that is accredited by an American standards body (such as the American National Standards Institute) or an equivalent international standards body in a process\u2014 (I) that is open to the public, including open for participation by any person; and (II) provides for a conflict resolution process; (ii) subject to an open comment and input process before being finalized by the standards development organization; (iii) consensus-based; and (iv) made publicly available once approved. (5) Cost related to the training The term cost related to the training means\u2014 (A) actual wages incurred for travel and attendance, including any necessary overtime pay and backfill wage; (B) travel expenses; (C) instructor expenses; or (D) facility costs and training materials. (6) Eligible entity The term eligible entity \u2014 (A) means\u2014 (i) a State or a Tribe; or (ii) an entity, including a public authority, board, or commission, established by 1 or more entities described in clause (i); and (B) does not include any entity that has failed to submit the certifications required under subsection (c)(5). (7) Emergency communications center (A) In general The term emergency communications center means\u2014 (i) a facility that\u2014 (I) is designated to receive a 9\u20131\u20131 request for emergency assistance; and (II) performs 1 or more of the functions described in subparagraph (B); or (ii) a public safety answering point, as defined in section 222 of the Communications Act of 1934 ( 47 U.S.C. 222 ). (B) Functions described The functions described in this subparagraph are the following: (i) Processing and analyzing 9\u20131\u20131 requests for emergency assistance and information and data related to such requests. (ii) Dispatching appropriate emergency response providers. (iii) Transferring or exchanging 9\u20131\u20131 requests for emergency assistance and information and data related to such requests with 1 or more other emergency communications centers and emergency response providers. (iv) Analyzing any communications received from emergency response providers. (v) Supporting incident command functions. (8) Emergency response provider The term emergency response provider has the meaning given the term in section 2 of the Homeland Security Act of 2002 ( 6 U.S.C. 101 ). (9) First Responder Network Authority The term First Responder Network Authority means the authority established under section 6204 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1424 ). (10) Interoperability The term interoperability means the capability of emergency communications centers to receive 9\u20131\u20131 requests for emergency assistance and information and data related to such requests, such as location information and callback numbers from a person initiating the request, then process and share the 9\u20131\u20131 requests for emergency assistance and information and data related to such requests with other emergency communications centers and emergency response providers without the need for proprietary interfaces and regardless of jurisdiction, equipment, device, software, service provider, or other relevant factors. (11) Nationwide public safety broadband network The term nationwide public safety broadband network has the meaning given the term in section 6001 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1401 ). (12) Next Generation 9\u20131\u20131 The term Next Generation 9\u20131\u20131 means an Internet Protocol-based system that\u2014 (A) ensures interoperability; (B) is secure; (C) employs commonly accepted standards; (D) enables emergency communications centers to receive, process, and analyze all types of 9\u20131\u20131 requests for emergency assistance; (E) acquires and integrates additional information useful to handling 9\u20131\u20131 requests for emergency assistance; and (F) supports sharing information related to 9\u20131\u20131 requests for emergency assistance among emergency communications centers and emergency response providers. (13) Reliability The term reliability means the employment of sufficient measures to ensure the ongoing operation of Next Generation 9\u20131\u20131 including through the use of geo-diverse, device- and network-agnostic elements that provide more than 1 route between end points with no common points where a single failure at that point would cause all to fail. (14) State The term State means any State of the United States, the District of Columbia, Puerto Rico, American Samoa, Guam, the United States Virgin Islands, the Northern Mariana Islands, and any other territory or possession of the United States. (15) Sustainable funding mechanism The term sustainable funding mechanism means a funding mechanism that provides adequate revenues to cover ongoing expenses, including operations, maintenance, and upgrades. (16) Tribe The term Tribe has the meaning given the term Indian Tribe in section 4(e) of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304(e) ). 160. Establishment of nationwide next generation 9\u20131\u20131 cybersecurity center The Assistant Secretary, after consulting with the Administrator and the Director of the Cybersecurity and Infrastructure Security Agency of the Department of Homeland Security, shall establish a Next Generation 9\u20131\u20131 Cybersecurity Center to coordinate with State, local, and regional governments on the sharing of cybersecurity information about, the analysis of cybersecurity threats to, and guidelines for strategies to detect and prevent cybersecurity intrusions relating to Next Generation 9\u20131\u20131. 161. Next generation 9\u20131\u20131 advisory board (a) Next generation 9\u20131\u20131 advisory board (1) Establishment The Assistant Secretary shall establish a Public Safety Next Generation 9\u20131\u20131 Advisory Board (in this section referred to as the Board ) to provide recommendations to the Assistant Secretary\u2014 (A) with respect to carrying out the duties and responsibilities of the Assistant Secretary in issuing the regulations required under section 159(c); (B) as required by paragraph (7); and (C) upon request under paragraph (8). (2) Membership (A) Voting members Not later than 150 days after the date of enactment of this section, the Assistant Secretary shall appoint 16 public safety members to the Board, of which\u2014 (i) 4 members shall represent local law enforcement officials; (ii) 4 members shall represent fire and rescue officials; (iii) 4 members shall represent emergency medical service officials; and (iv) 4 members shall represent 9\u20131\u20131 professionals. (B) Diversity of membership Members shall be representatives of States or Tribes and local governments, chosen to reflect geographic and population density differences as well as public safety organizations at the national level across the United States. (C) Expertise All members shall have specific expertise necessary for developing technical requirements under this section, such as technical expertise, and expertise related to public safety communications and 9\u20131\u20131 services. (D) Rank and file members In making the appointments required by subparagraph (A), the Assistant Secretary shall appoint a rank and file member from each of the public safety disciplines listed in clauses (i) through (iv) of subparagraph (A) as a member of the Board and shall select such member from an organization that represents its public safety discipline at the national level. (3) Period of Appointment (A) In general Except as provided in subparagraph (B), members of the Board shall serve for a 3-year term. (B) Removal for cause A member of the Board may be removed for cause upon the determination of the Assistant Secretary. (4) Vacancies Any vacancy in the Board shall be filled in the same manner as the original appointment. (5) Quorum A majority of the members of the Board shall constitute a quorum. (6) Chairperson and vice chairperson The Board shall select a Chairperson and Vice Chairperson from among the voting members of the Board. (7) Duty of board to submit recommendations Not later than 120 days after all members of the Board are appointed under paragraph (2), the Board shall submit to the Assistant Secretary recommendations for\u2014 (A) deploying Next Generation 9\u20131\u20131 in rural and urban areas; (B) ensuring flexibility in guidance, rules, and grant funding to allow for technology improvements; (C) creating efficiencies related to Next Generation 9\u20131\u20131, including cybersecurity and the virtualization and sharing of core infrastructure; (D) enabling effective coordination among State, local, Tribal, and territorial government entities to ensure that the needs of emergency communications centers in both rural and urban areas are taken into account in each implementation plan required under section 159(c)(3)(A)(iii); and (E) incorporating existing cybersecurity resources into Next Generation 9\u20131\u20131 procurement and deployment. (8) Authority to provide additional recommendations Except as provided in paragraphs (1) and (7), the Board may provide recommendations to the Assistant Secretary only upon request of the Assistant Secretary. (9) Duration of authority The Board shall terminate on the date on which funds made available to make grants under section 159(c) are no longer available to be expended. (b) Rule of construction Nothing in this section may be construed as limiting the authority of the Assistant Secretary to seek comment from stakeholders and the public. 162. Authorization of appropriations (a) In general There are authorized to be appropriated to the Assistant Secretary to carry out sections 159, 160, and 161 such sums as may be necessary for fiscal years 2027 through 2031, and such amounts are authorized to remain available until expended. (b) Administrative costs Not more than 4 percent of any amounts appropriated under subsection (a) may be used for administrative purposes (including carrying out sections 160 and 161). .",
      "versionDate": "2026-03-11",
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
        "actionDate": "2026-01-15",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "6505",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Next Generation 9\u20131\u20131 Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2026-03-30T15:22:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-11",
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
          "measure-id": "id119s4062",
          "measure-number": "4062",
          "measure-type": "s",
          "orig-publish-date": "2026-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4062v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2026-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Next Generation 9\u20131\u20131 Act</strong></p><p>This bill establishes a grant program to support implementation of next generation 9-1-1 (NG9-1-1) systems by state, territorial, and tribal governments and requires other related activities. <em>NG9-1-1</em> means a secure, interoperable, Internet Protocol-based (IP-based) system for receiving 9-1-1 requests for emergency assistance. (IP-based 9-1-1 systems have capabilities that legacy telephone systems do not, including enhanced location-finding and the ability to receive text and multimedia messages.)</p><p>Under the bill, the National Telecommunications and Information Administration (NTIA) must provide grants to state, territorial, and tribal governments (and entities established by those governments) to support the implementation and maintenance of NG9-1-1 systems. Grant funds may also be used for public outreach on NG9-1-1, implementation of cybersecurity measures, and, subject to certain limits, training and administrative costs.</p><p>Entities applying for grants must submit a plan for NG9-1-1 coordination and implementation that ensures interoperability and reliability, incorporates cybersecurity tools, and meets other requirements related to technology and procurement. Applicants must also certify that they have established, or will establish within a specified time frame, a sustainable funding mechanism to support NG9-1-1 and effective cybersecurity resources.</p><p>The NTIA must advise applicants on the preparation of implementation plans and provide technical assistance to grant recipients.</p><p>Further, the NTIA must establish (1) an advisory board to provide recommendations with respect to the grant program and other topics related to NG9-1-1; and (2) a cybersecurity center to coordinate with state, local, and regional governments on the sharing of cybersecurity information related to NG9-1-1.</p>"
        },
        "title": "Next Generation 9\u20131\u20131 Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4062.xml",
    "summary": {
      "actionDate": "2026-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Next Generation 9\u20131\u20131 Act</strong></p><p>This bill establishes a grant program to support implementation of next generation 9-1-1 (NG9-1-1) systems by state, territorial, and tribal governments and requires other related activities. <em>NG9-1-1</em> means a secure, interoperable, Internet Protocol-based (IP-based) system for receiving 9-1-1 requests for emergency assistance. (IP-based 9-1-1 systems have capabilities that legacy telephone systems do not, including enhanced location-finding and the ability to receive text and multimedia messages.)</p><p>Under the bill, the National Telecommunications and Information Administration (NTIA) must provide grants to state, territorial, and tribal governments (and entities established by those governments) to support the implementation and maintenance of NG9-1-1 systems. Grant funds may also be used for public outreach on NG9-1-1, implementation of cybersecurity measures, and, subject to certain limits, training and administrative costs.</p><p>Entities applying for grants must submit a plan for NG9-1-1 coordination and implementation that ensures interoperability and reliability, incorporates cybersecurity tools, and meets other requirements related to technology and procurement. Applicants must also certify that they have established, or will establish within a specified time frame, a sustainable funding mechanism to support NG9-1-1 and effective cybersecurity resources.</p><p>The NTIA must advise applicants on the preparation of implementation plans and provide technical assistance to grant recipients.</p><p>Further, the NTIA must establish (1) an advisory board to provide recommendations with respect to the grant program and other topics related to NG9-1-1; and (2) a cybersecurity center to coordinate with state, local, and regional governments on the sharing of cybersecurity information related to NG9-1-1.</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119s4062"
    },
    "title": "Next Generation 9\u20131\u20131 Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Next Generation 9\u20131\u20131 Act</strong></p><p>This bill establishes a grant program to support implementation of next generation 9-1-1 (NG9-1-1) systems by state, territorial, and tribal governments and requires other related activities. <em>NG9-1-1</em> means a secure, interoperable, Internet Protocol-based (IP-based) system for receiving 9-1-1 requests for emergency assistance. (IP-based 9-1-1 systems have capabilities that legacy telephone systems do not, including enhanced location-finding and the ability to receive text and multimedia messages.)</p><p>Under the bill, the National Telecommunications and Information Administration (NTIA) must provide grants to state, territorial, and tribal governments (and entities established by those governments) to support the implementation and maintenance of NG9-1-1 systems. Grant funds may also be used for public outreach on NG9-1-1, implementation of cybersecurity measures, and, subject to certain limits, training and administrative costs.</p><p>Entities applying for grants must submit a plan for NG9-1-1 coordination and implementation that ensures interoperability and reliability, incorporates cybersecurity tools, and meets other requirements related to technology and procurement. Applicants must also certify that they have established, or will establish within a specified time frame, a sustainable funding mechanism to support NG9-1-1 and effective cybersecurity resources.</p><p>The NTIA must advise applicants on the preparation of implementation plans and provide technical assistance to grant recipients.</p><p>Further, the NTIA must establish (1) an advisory board to provide recommendations with respect to the grant program and other topics related to NG9-1-1; and (2) a cybersecurity center to coordinate with state, local, and regional governments on the sharing of cybersecurity information related to NG9-1-1.</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119s4062"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4062is.xml"
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
      "title": "Next Generation 9\u20131\u20131 Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Next Generation 9\u20131\u20131 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Telecommunications and Information Administration Organization Act to provide for further deployment and coordination of Next Generation 9-1-1, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T04:03:35Z"
    }
  ]
}
```
