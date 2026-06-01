# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4300?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4300
- Title: JOAN Act
- Congress: 119
- Bill type: S
- Bill number: 4300
- Origin chamber: Senate
- Introduced date: 2026-04-15
- Update date: 2026-05-13T17:35:43Z
- Update date including text: 2026-05-13T17:35:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in Senate
- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-04-15: Introduced in Senate

## Actions

- 2026-04-15 - IntroReferral: Introduced in Senate
- 2026-04-15 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4300",
    "number": "4300",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "JOAN Act",
    "type": "S",
    "updateDate": "2026-05-13T17:35:43Z",
    "updateDateIncludingText": "2026-05-13T17:35:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T17:12:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4300is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4300\nIN THE SENATE OF THE UNITED STATES\nApril 15 (legislative day, April 14), 2026 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo promote interagency coordination for reviewing certain authorizations under the Natural Gas Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Jurisdictional Oversight and Adjudication for Natural Gas Act or the JOAN Act .\n#### 2. Promoting interagency coordination for review of natural gas infrastructure\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(2) Federal authorization**\nThe term Federal authorization has the meaning given that term in section 15(a) of the Natural Gas Act ( 15 U.S.C. 717n(a) ).\n**(3) NEPA review**\nThe term NEPA review means the process of reviewing a proposed Federal action under section 102 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332 ).\n**(4) Project-related NEPA review**\nThe term project-related NEPA review means any NEPA review required to be conducted with respect to the issuance of an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ).\n##### (b) Commission NEPA review responsibilities\nIn acting as the lead agency under section 15(b)(1) of the Natural Gas Act ( 15 U.S.C. 717n(b)(1) ) for the purposes of complying with the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) with respect to an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ), the Commission shall, in accordance with this section and other applicable Federal law\u2014\n**(1)**\nbe the only lead agency;\n**(2)**\ncoordinate as early as practicable with each agency designated as a participating agency under subsection (d)(3) to ensure that the Commission develops information in conducting its project-related NEPA review that is reasonably required by the participating agency in considering an aspect of an application for a Federal authorization for which the agency is responsible; and\n**(3)**\ntake such actions as are necessary and proper to facilitate the expeditious resolution of its project-related NEPA review.\n##### (c) Deference to Commission\nIn making a decision with respect to a Federal authorization required with respect to an application for authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ), each agency shall give deference, to the maximum extent authorized by law, to the scope of the project-related NEPA review that the Commission determines to be appropriate.\n##### (d) Participating agencies\n**(1) Identification**\nThe Commission shall identify, not later than 30 days after the Commission receives an application for an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ), any Federal or State agency, local government, or Indian Tribe that may issue a Federal authorization or is required by Federal law to consult with the Commission in conjunction with the issuance of a Federal authorization required for such authorization or certificate.\n**(2) Invitation**\n**(A) In general**\nNot later than 45 days after the Commission receives an application for an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ), the Commission shall invite any agency identified under paragraph (1) to participate in the review process for the applicable Federal authorization.\n**(B) Deadline**\nAn invitation issued under subparagraph (A) shall establish a deadline by which a response to the invitation shall be submitted to the Commission, which may be extended by the Commission for good cause.\n**(3) Designation as participating agencies**\nNot later than 60 days after the Commission receives an application for an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ), the Commission shall designate an agency identified under paragraph (1) as a participating agency with respect to an application for authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ) unless the agency informs the Commission, in writing, by the deadline established pursuant to paragraph (2)(B), that the agency\u2014\n**(A)**\nhas no jurisdiction or authority with respect to the applicable Federal authorization;\n**(B)**\nhas no special expertise or information relevant to any project-related NEPA review; or\n**(C)**\ndoes not intend to submit comments for the record for the project-related NEPA review conducted by the Commission.\n**(4) Effect of designation and non-designation**\nDesignation or non-designation of an agency as a participating agency under paragraph (3) with respect to an application for an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ) may not serve as evidence of an incomplete record before a court.\n##### (e) Water quality impacts\n**(1) In general**\nNotwithstanding section 401 of the Federal Water Pollution Control Act ( 33 U.S.C. 1341 ), an applicant for a Federal authorization shall not be required to provide a certification under such section with respect to the Federal authorization.\n**(2) Coordination**\nWith respect to any NEPA review for a Federal authorization to conduct an activity that will directly result in a discharge into the navigable waters (within the meaning of the Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. )), the Commission shall identify as an agency under subsection (d)(1) the State in which the discharge originates or will originate, or, if appropriate, the interstate water pollution control agency having jurisdiction over the navigable waters at the point where the discharge originates or will originate.\n**(3) Proposed conditions**\nA State or interstate agency designated as a participating agency pursuant to paragraph (2) may propose to the Commission terms or conditions for inclusion in an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ) that the State or interstate agency determines are necessary to ensure that any activity described in paragraph (2) conducted pursuant to such authorization or certification will comply with the applicable provisions of sections 301, 302, 303, 306, and 307 of the Federal Water Pollution Control Act ( 33 U.S.C. 1311 , 1312, 1313, 1316, 1317).\n**(4) Commission consideration of conditions**\nThe Commission may include a term or condition in an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ) proposed by a State or interstate agency under paragraph (3) only if the Commission finds that the term or condition is necessary to ensure that any activity described in paragraph (2) conducted pursuant to such authorization or certification will comply with the applicable provisions of sections 301, 302, 303, 306, and 307 of the Federal Water Pollution Control Act ( 33 U.S.C. 1311 , 1312, 1313, 1316, 1317).\n##### (f) Schedule\n**(1) Deadline for Federal authorizations**\nA deadline for a Federal authorization required with respect to an application for authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ) set by the Commission under section 15(c)(1) of such Act ( 15 U.S.C. 717n(c)(1) ) shall be not later than 90 days after the Commission completes its project-related NEPA review, unless an applicable schedule is otherwise established by Federal law.\n**(2) Concurrent reviews**\nEach Federal and State agency\u2014\n**(A)**\nthat may consider an application for a Federal authorization required with respect to an application for authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ) shall formulate and implement a plan for administrative, policy, and procedural mechanisms to enable the agency to ensure completion of Federal authorizations in compliance with schedules established by the Commission under section 15(c)(1) of such Act ( 15 U.S.C. 717n(c)(1) ); and\n**(B)**\nin considering an aspect of an application for a Federal authorization required with respect to an application for authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ), shall\u2014\n**(i)**\nformulate and implement a plan to enable the agency to comply with the schedule established by the Commission under section 15(c)(1) of such Act ( 15 U.S.C. 717n(c)(1) );\n**(ii)**\ncarry out the obligations of that agency under applicable law concurrently, and in conjunction with, the project-related NEPA review conducted by the Commission, and in compliance with the schedule established by the Commission under section 15(c)(1) ( 15 U.S.C. 717n(c)(1) ) of such Act, unless the agency notifies the Commission in writing that doing so would impair the ability of the agency to conduct needed analysis or otherwise carry out such obligations;\n**(iii)**\ntransmit to the Commission a statement\u2014\n**(I)**\nacknowledging receipt of the schedule established by the Commission under section 15(c)(1) of the Natural Gas Act ( 15 U.S.C. 717n(c)(1) ); and\n**(II)**\nsetting forth the plan formulated under clause (i) of this subparagraph;\n**(iv)**\nnot later than 30 days after the agency receives such application for a Federal authorization, transmit to the applicant a notice\u2014\n**(I)**\nindicating whether such application is ready for processing; and\n**(II)**\nif such application is not ready for processing, that includes a comprehensive description of the information needed for the agency to determine that the application is ready for processing;\n**(v)**\ndetermine that such application for a Federal authorization is ready for processing for purposes of clause (iv) if such application is sufficiently complete for the purposes of commencing consideration, regardless of whether supplemental information is necessary to enable the agency to complete the consideration required by law with respect to such application; and\n**(vi)**\nnot less often than once every 90 days, transmit to the Commission a report describing the progress made in considering such application for a Federal authorization.\n**(3) Failure to meet deadline**\nIf a Federal or State agency, including the Commission, fails to meet a deadline for a Federal authorization set forth in the schedule established by the Commission under section 15(c)(1) of the Natural Gas Act ( 15 U.S.C. 717n(c)(1) ), not later than 5 days after such deadline, the head of the relevant Federal agency (including, in the case of a failure by a State agency, the Federal agency overseeing the delegated authority) shall notify Congress and the Commission of such failure and set forth a recommended implementation plan to ensure completion of the action to which such deadline applied.\n##### (g) Consideration of applications for Federal authorization\n**(1) Issue identification and resolution**\n**(A) Identification**\nFederal and State agencies that may consider an aspect of an application for a Federal authorization shall identify, as early as possible, any issues of concern that may delay or prevent an agency from working with the Commission to resolve such issues and granting such authorization.\n**(B) Issue resolution**\nThe Commission may forward any issue of concern identified under subparagraph (A) to the heads of the relevant agencies (including, in the case of an issue of concern that is a failure by a State agency, the Federal agency overseeing the delegated authority, if applicable) for resolution.\n**(2) Remote surveys**\n**(A) In general**\nIf a Federal or State agency considering an aspect of an application for a Federal authorization requires the person applying for such authorization to submit data, the agency shall consider any such data gathered by aerial or other remote means that the person submits.\n**(B) Conditional approval**\nThe agency may grant a conditional approval for the Federal authorization based on data gathered by aerial or remote means, conditioned on the verification of such data by subsequent onsite inspection.\n**(3) Application processing**\nThe Commission, and Federal and State agencies, may allow a person applying for a Federal authorization to fund a third-party contractor to assist in reviewing the application for such authorization.\n##### (h) Accountability, transparency, efficiency\nFor an application for an authorization under section 3 of the Natural Gas Act ( 15 U.S.C. 717b ) or a certificate of public convenience and necessity under section 7 of such Act ( 15 U.S.C. 717f ) that requires multiple Federal authorizations, the Commission, with input from any Federal or State agency considering an aspect of the application, shall track and make available to the public on the website of the Commission information related to the actions required to complete the Federal authorizations. Such information shall include the following:\n**(1)**\nThe schedule established by the Commission under section 15(c)(1) of the Natural Gas Act ( 15 U.S.C. 717n(c)(1) ).\n**(2)**\nA list of all the actions required by each applicable agency to complete permitting, reviews, and other actions necessary to obtain a final decision on the application.\n**(3)**\nThe expected completion date for each such action.\n**(4)**\nA point of contact at the agency responsible for each such action.\n**(5)**\nIn the event that an action is still pending as of the expected date of completion, a brief explanation of the reasons for the delay.\n#### 3. Acceleration of claims\n##### (a) Definitions\nIn this section:\n**(1) Civil action**\nThe term civil action means an initial claim challenging a core authorization for a covered project.\n**(2) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(3) Core authorization**\nThe term core authorization means a Federal authorization issued pursuant to section 3(e) or section 7(c) of the Natural Gas Act ( 15 U.S.C. 717b(e) , 717f(c)).\n**(4) Covered project**\nThe term covered project means a project requiring a core authorization.\n**(5) Federal authorization**\nThe term Federal authorization means any license, permit, approval, finding, determination, or administrative decision issued by an agency, and any interagency consultation that is required or authorized under Federal law, to site, construct, reconstruct, abandon, or commence operations of a covered project administered by\u2014\n**(A)**\na Federal agency; or\n**(B)**\nin the case of a State participating in or administering a review required or authorized under Federal law, as applicable, a State agency.\n**(6) Project sponsor**\nThe term project sponsor means any person, including a State, Tribal, or local government entity, that\u2014\n**(A)**\nis an applicant for, or holder of, a core authorization or any other Federal authorization for a covered project; or\n**(B)**\notherwise proposes to site, construct, reconstruct, own, or operate a covered project.\n**(7) Related claim**\nThe term related claim means a claim challenging a Federal authorization that is joined to a civil action after that civil action has been filed.\n##### (b) Final agency action\nNotwithstanding any other provision of law, issuance of a core authorization for a covered project shall be considered a final agency action for the purposes of chapter 7 of title 5, United States Code, with respect to all Federal authorizations required for that covered project.\n##### (c) Claims\n**(1) Sole and exclusive relief**\n**(A) In general**\nThe filing and final adjudication of a civil action shall constitute the sole and exclusive means of judicial review and relief with respect to the applicable covered project and all Federal authorizations issued for that covered project.\n**(B) Bar on subsequent actions**\nAfter the final adjudication of a civil action, any subsequent cause of action or challenge, whether statutory, procedural, or substantive, related to or connected with the applicable covered project or any Federal authorization for that covered project brought by any party except the project sponsor shall be barred and dismissed for lack of jurisdiction.\n**(2) Venue**\n**(A) In general**\nA civil action shall be filed exclusively in\u2014\n**(i)**\nthe United States Court of Appeals for the District of Columbia Circuit; or\n**(ii)**\nthe court of appeals of the United States for the judicial circuit in which the principal place of business of the project sponsor for the applicable covered project is located.\n**(B) Related claims**\nAfter a civil action is filed in an applicable court described in subparagraph (A), all related claims arising out of the same nucleus of operative fact as that civil action shall be joined or consolidated to that court for adjudication.\n**(3) Time to file**\nA civil action and all related claims arising out of the same nucleus of operative fact shall be filed with the applicable court by the earlier of\u2014\n**(A)**\nthe date that is 60 days after the core authorization is published in the Federal Register; and\n**(B)**\nthe statutory deadline required for causes of action relating to that core authorization.\n**(4) Judicial review**\n**(A) In general**\nSubject to subsection (d), the filing and final adjudication of a civil action shall constitute the only opportunity for judicial review of the applicable covered project and all Federal authorizations issued for that covered project.\n**(B) Scope**\nJudicial review of a civil action and any related claim arising out of the same nucleus of operative fact under this section\u2014\n**(i)**\nshall\u2014\n**(I)**\nbe limited to the finalized consolidated record under subsection (g)(3)(C); and\n**(II)**\nbe based exclusively on that finalized consolidated record; and\n**(ii)**\nshall not take evidence, permit discovery, receive testimony, or engage in fact-finding.\n**(C) Preliminary injunctions**\n**(i) Multiplicative merit standard**\nIn any civil action seeking a preliminary injunction or a temporary restraining order to halt a Federal action based on an alleged violation of this Act, the applicable court shall determine the likelihood of success on the merits by calculating the cumulative probability of success across all independent legal and jurisdictional requirements.\n**(ii) Probabilistic calculation**\nA court may not find a likelihood of success on the merits under clause (i) unless the product of the probabilities of success for each independent legal and jurisdictional requirement, including standing under article III of the Constitution of the United States, final agency action, and the merits of the underlying claim, exceeds 50 percent.\n**(iii) Written findings**\nThe court under clause (ii) shall issue written findings of fact and conclusions of law specifying\u2014\n**(I)**\nthe estimated probability of success assigned to each independent legal and jurisdictional requirement; and\n**(II)**\nthe cumulative probability of success.\n**(D) Deadline**\nIf the applicable court does not issue a final determination for a filed civil action and all related claims arising out of the same nucleus of operative fact by the date that is 180 days after the expiration of the applicable timeline described in paragraph (3), the core authorization and all associated Federal authorizations for the applicable covered project shall be considered approved and not subject to further review.\n**(E) Identification of factual determinations**\nFor the purposes of judicial review, the statements of material fact submitted under subsection (g)(2) shall not constitute independent evidence or a freestanding factual determination apart from the cited administrative record material.\n**(5) Relief**\n**(A) In general**\nIn reviewing a civil action, the applicable court may not\u2014\n**(i)**\nissue an injunction lasting for a period exceeding 60 days;\n**(ii)**\nenjoin any covered project activity unrelated to a specific issue identified by the court; or\n**(iii)**\ngrant permanent injunctive relief unless the plaintiff demonstrates by clear and convincing evidence that\u2014\n**(I)**\nthe plaintiff has suffered an irreparable injury;\n**(II)**\nremedies available at law, including monetary damages, are inadequate to compensate for the irreparable injury;\n**(III)**\nconsidering the balance of hardships between the plaintiff and defendant, a remedy in equity is warranted; and\n**(IV)**\nthe public interest would not be disserved by a permanent injunction.\n**(B) Permanent injunction**\nAny permanent injunction issued by a court pursuant to this subsection shall be supported by a finding, by clear and convincing evidence, of extraordinary circumstances, and shall be as narrowly tailored as possible to correct the injury and the least intrusive means necessary to correct the injury.\n**(C) Security for injunctive relief**\nAny court issuing a temporary restraining order or preliminary injunction in a civil action under this section shall require the movant to provide security in an amount that the court considers proper to pay the costs and damages sustained by any party found to have been wrongfully enjoined or restrained, consistent with rule 65(c) of the Federal Rules of Civil Procedure.\n**(6) No remand with vacatur**\nIn reviewing a civil action, the applicable court may not issue a remedy of remand with vacatur.\n**(7) Project segmentation**\nAfter the filing of a civil action, the project sponsor for the implicated covered project may continue construction for any part of the covered project that is unaffected by the civil action.\n**(8) Prohibited civil actions**\nA civil action may not be filed by any party that did not raise the issue giving rise to that civil action during the notice and comment period for the applicable Federal authorization.\n##### (d) Project sponsor exception\n**(1) In general**\nNotwithstanding subsection (c), a project sponsor may bring a separate claim challenging a Federal authorization for an applicable covered project regardless of whether a civil action concerning that Federal authorization has been filed and adjudicated, subject to the condition that the specific underlying issue of that separate claim has not previously been finally adjudicated.\n**(2) No related claims**\nA claim described in paragraph (1) may not be joined by a related claim or any other claim arising out of the same nucleus of operative fact.\n##### (e) Effect on substantive standards\nNothing in this section alters substantive environmental requirements or reduces opportunities for public comment under applicable Federal law.\n##### (f) Multiple core authorizations\nIf more than 1 Federal agency issues a core authorization for a covered project, the Commission shall be the lead agency for purposes of an environmental review for the covered project under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), if applicable.\n##### (g) Statement of material facts and technical findings\n**(1) Definition of statement of material fact**\nIn this subsection, the term statement of material fact means a citation index identifying, by specific record citation, the portions of the administrative record that set forth the material factual determinations and technical conclusions relied on in a Federal authorization for a covered project.\n**(2) Transmission**\nNot later than 60 days after the date of publication of a core authorization in the Federal Register, each Federal agency that issued, or is required to issue, a Federal authorization for the applicable covered project shall submit to the Commission\u2014\n**(A)**\nthe administrative record for that Federal authorization; and\n**(B)**\na statement of material fact and technical conclusions that identifies, by specific citation to the administrative record, the portions of the record containing the material factual determinations and technical conclusions relied on by the Federal agency.\n**(3) Consolidated administrative record**\n**(A) Consolidate and publish**\nNot later than 90 days after the date of publication of a core authorization in the Federal Register, the Commission shall\u2014\n**(i)**\nconsolidate the submissions under paragraph (2) (referred to in this subsection as the consolidated administrative record ); and\n**(ii)**\npublish a notice of availability of the consolidated administrative record.\n**(B) Objections**\n**(i) In general**\nNot later than 30 days after the date of publication of the notice under subparagraph (A), any party may submit to the Commission a written objection limited to whether the consolidated administrative record omits materials\u2014\n**(I)**\nthat were before the Federal agency; and\n**(II)**\nthat were directly or indirectly considered in issuing a Federal authorization.\n**(ii) No merits**\nAn objection to the consolidated administrative record submitted under clause (i) may not\u2014\n**(I)**\nraise merit arguments; or\n**(II)**\nseek discovery, testimony, or new evidence.\n**(iii) Resolution**\nNot later than 60 days after the date of publication of the notice under subparagraph (A), the Commission shall resolve each objection to the consolidated administrative record submitted under clause (i) and, as necessary, direct limited supplementation of the consolidated administrative record by the relevant Federal agency.\n**(C) Closure**\nAfter all objections to the consolidated administrative record are resolved under subparagraph (B)(iii)\u2014\n**(i)**\nthe consolidated administrative record shall be considered final and closed; and\n**(ii)**\nthe Commission shall issue a public written order indicating the consolidated administrative record is finalized and closed.\n**(D) Final agency action**\nThe written order of the Commission under subparagraph (C)(ii) shall constitute a final agency action for the purposes of chapter 7 of title 5, United States Code, solely with respect to the contents and completeness of the consolidated administrative record.",
      "versionDate": "2026-04-15",
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
        "name": "Energy",
        "updateDate": "2026-05-13T17:35:42Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4300is.xml"
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
      "title": "JOAN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "JOAN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Jurisdictional Oversight and Adjudication for Natural Gas Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote interagency coordination for reviewing certain authorizations under the Natural Gas Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:58Z"
    }
  ]
}
```
