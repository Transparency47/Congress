# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3918?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3918
- Title: Government Surveillance Transparency Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3918
- Origin chamber: Senate
- Introduced date: 2026-02-25
- Update date: 2026-03-16T15:21:40Z
- Update date including text: 2026-03-16T15:21:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in Senate
- 2026-02-25 - IntroReferral: Introduced in Senate
- 2026-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-02-25: Introduced in Senate

## Actions

- 2026-02-25 - IntroReferral: Introduced in Senate
- 2026-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3918",
    "number": "3918",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Government Surveillance Transparency Act of 2026",
    "type": "S",
    "updateDate": "2026-03-16T15:21:40Z",
    "updateDateIncludingText": "2026-03-16T15:21:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T20:09:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "MT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "UT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3918is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3918\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2026 Mr. Wyden (for himself, Mr. Daines , Mr. Lee , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to require that notice of criminal surveillance orders be eventually provided to targets, to reform the use of non-disclosure orders to providers, to prohibit indefinite sealing of criminal surveillance orders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Government Surveillance Transparency Act of 2026 .\n#### 2. Criminal surveillance orders\n##### (a) In general\nPart II of title 18, United States Code, is amended by inserting after chapter 206 the following:\n206A Criminal surveillance orders Sec. 3131. Definitions. 3132. Criminal surveillance orders. 3133. Request for unsealing or challenging redactions. 3131. Definitions In this chapter: (1) Application The term application \u2014 (A) means an application for a criminal surveillance order; and (B) includes all supporting affidavits and exhibits. (2) Pen register; trap and trace device The terms pen register , and trap and trace device have the meanings given the terms in section 3127. (3) Criminal surveillance order The term criminal surveillance order means\u2014 (A) an order authorizing or approving the interception of a wire communication, oral communication, or electronic communication under chapter 119 or under an equivalent State law; (B) an order authorizing or approving the installation and use of a pen register or a trap and trace device under chapter 206 or under an equivalent State law; (C) an order for the installation of a mobile tracking device under section 3117; (D) an order for disclosure under chapter 121; (E) an order for a delay of notification or nondisclosure under section 2705; (F) a search or seizure warrant issued using the procedures described in the Federal Rules of Criminal Procedure or in the case of a State or Tribal court, issued using State or Tribal warrant procedures; (G) in the case of a court-martial or other proceeding under chapter 47 of title 10 (Uniform Code of Military Justice), a warrant or order issued under section 846 of that title; (H) a warrant under section 3103a; (I) an order under section 1651 of title 28; (J) an order for third party assistance under section 2518(4) or section 3124; or (K) an order to enforce the assistance capability and capacity requirements under section 2522. (4) Electronic communication; oral communication; wire communication The terms electronic communication , oral communication , and wire communication have the meanings given the terms in section 2510. (5) Indian Tribe The term Indian Tribe has the meaning given such term in section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 ). (6) Inventory The term inventory means the inventory and other materials\u2014 (A) returned to a Federal, State, or Tribal court or a court-martial or other proceeding under chapter 47 of title 10 (Uniform Code of Military Justice) in connection with the execution of a criminal surveillance order (including under paragraph (1)(D) or (2)(B) of rule 41(f) of the Federal Rules of Criminal Procedure, under comparable State warrant procedures, or under procedures applicable to a court-martial or other proceeding under chapter 47 of title 10); or (B) provided to persons and other parties described in section 2518(8)(d). (7) State The term State means each of the several States of the United States, the District of Columbia, the Commonwealth of Puerto Rico, American Samoa, the Commonwealth of the Northern Mariana Islands, Guam, and the United States Virgin Islands. (8) Substantially prevails The term substantially prevails has the meaning given the term in section 552(a)(4)(E) of title 5. 3132. Criminal surveillance orders (a) Limitation on sealing (1) In general Except as provided in paragraph (2), a court may not seal a criminal surveillance order, application, or inventory for a period that extends after the later of\u2014 (A) date the order is executed; or (B) the date on which the authorized surveillance ends. (2) Exceptions (A) In general An applicant for a criminal surveillance order may file a written request for the court to seal the criminal surveillance order, the application, or the inventory for a period not to exceed 180 days after the later of the date the order is executed or the date on which the authorized surveillance ends, which request the court shall grant if the applicant certifies that there is reason to believe that failure to seal will have an adverse result described in subparagraph (B). (B) Adverse result (i) In general An adverse result described in this subparagraph is\u2014 (I) endangering the life or physical safety of an individual; (II) flight from prosecution; (III) destruction of or tampering with evidence; (IV) intimidation of potential witnesses; or (V) otherwise seriously jeopardizing the investigation to which the criminal surveillance order relates or unduly delaying a trial resulting from the investigation. (ii) Other requirements (I) In general When certifying an adverse result, the applicant shall certify that there is reason to believe that the person whose information is targeted by the order does not know\u2014 (aa) about the investigation; and (bb) that they are a target or person of interest in the investigation. (II) Failure to certify If the applicant does not satisfy the requirements of subclause (I)\u2014 (aa) the applicant must follow the higher standard of judicial review required by subparagraph (C)(ii); and (bb) the failure to satisfy such requirements shall be disclosed in both the criminal surveillance order and any preclusion of notice order issued for that criminal surveillance order. (iii) Review by court The court may, in its discretion, require the government to provide the factual basis for the certification described in clause (i) and may review that factual basis for sufficiency. (iv) Notification (I) In general For any criminal surveillance order, application, or inventory that is sealed at the Government\u2019s request, the Government shall promptly notify the court if the Government no longer has reason to believe that removal of a seal will have an adverse result described in this subparagraph. (II) Unsealing After being notified by the Government under subclause (I), the court shall unseal the criminal surveillance order, application, or inventory. (C) Extensions (i) In general The court may grant a single extension of a sealing order for up to 180 days, upon the applicant\u2019s motion, based on a renewed certification that failure to extend the sealing period will have an adverse result described in subparagraph (B). (ii) Heightened judicial review of subsequent extensions (I) In general For any extension after an extension under clause (i), the court may grant an extension of a sealing order for up to 180 days, upon the applicant\u2019s motion, if the applicant\u2014 (aa) demonstrates\u2014 (AA) a particularized showing that failure to extend the sealing period will have an adverse result described in subparagraph (B); and (BB) a particularized showing that the adverse result would not be avoided by redaction of specified words, phrases, or passages in the criminal surveillance order, application, or inventory; and (bb) details\u2014 (AA) the nature of the investigation; (BB) the suspected crimes; (CC) the name of the target; and (DD) specific facts that substantiate the need for the extension. (II) Redacted documents (aa) In general If the court determines that an applicant has met the requirements of subitem (AA) of subclause (I)(aa), but not the requirements of subitem (BB) of subclause (I)(aa), the court shall order the applicant to submit proposed redactions to each sealed document. (bb) Disposition After considering the proposed redactions of the applicant, if any, the court may order the applicant to refile 1 or more sealed documents with such redactions as the court finds appropriate, direct the clerk to unseal the entirety of 1 or more sealed documents, or order that 1 or more sealed documents remain under seal. (D) Sealing of rejected applications and unexecuted criminal surveillance orders A court may, pursuant to subparagraph (A), seal an unexecuted criminal surveillance order, or a rejected application. (E) Challenge of adverse result certification or extension (i) In general Any person seeking to unseal a surveillance order, application, or inventory may challenge\u2014 (I) a certification of the adverse result under this paragraph; or (II) the particularized showings and detailed information necessary for a second and subsequent extension. (ii) Heightened standard If an order under this paragraph is issued earlier than 1 year before the date on which a challenge under clause (i) is made, the requirements of subparagraph (C)(ii) shall apply to a warrant or order sealed in accordance with chapter 206A. (iii) Costs If a person substantially prevails in a challenge under this subparagraph, the court shall order the applicant for the criminal surveillance order at issue to pay the litigation costs of the person (including reasonable attorney's fees). (b) Docketing and publication of criminal surveillance orders, applications, inventories, and associated docket records (1) Docket records Except as provided in paragraph (2), regardless of whether a court seals a criminal surveillance order or application under this section, the public docket record for any criminal surveillance case shall\u2014 (A) be made available as an open Government data asset and under an open license, as such terms are defined in section 3502 of title 44, and in a manner that facilitates downloading docket records in bulk, in accordance with rules promulgated by the Judicial Conference of the United States, after consultation with the National Institute of Standards and Technology, the Administrator of General Services, the Electronic Public Access Public User Group, private entities offering electronic case management software, the National Center for State Courts, and the National American Indian Court Judges Association, on the website of the court; and (B) include, at a minimum\u2014 (i) the date and time the application was filed, the order was entered, and the warrant was returned to the court, where applicable; (ii) the type of order, including\u2014 (I) the statutory authority under which the order was issued; (II) the type of crime under investigation; (III) the investigating agency; (IV) the duration of the requested surveillance if any; (V) whether sealing and deferred notice were requested, if so for how long; (VI) whether an order for third party assistance was requested; and (VII) disposition by the court, whether granted, modified, or denied; (iii) an index describing any subsequent filings or orders related to the case; (iv) the unique case number in accordance with paragraph (3); and (v) the date on which the seal will expire (unless extended pursuant to subsection (a)(2)(C)). (2) Showing of adverse result If an applicant in a sealed case demonstrates that public disclosure of any docket item listed in paragraph (1)(B)(ii) will have an adverse result described in subsection (a)(2)(B), the court may direct the clerk to withhold that item from the public docket record until the sealing order expires. (3) Case number and caption (A) In general A court shall assign for each application\u2014 (i) a unique case number for every identified target, including for each unique street address, parcel, person, phone number, device, or account targeted; and (ii) a case caption providing only generic information about the type of order sought and the target of the order. (B) Requirements A court shall assign a case number and case caption under subparagraph (A) in accordance with rules promulgated by the Judicial Conference of the United States, in consultation with the Electronic Public Access Public User Group, or in the case of a State court, in accordance with rules promulgated by the highest court of the State, and in the case of a Tribal court, in accordance with rules promulgated by the highest court of the Indian Tribe. (4) Compliance with the Rehabilitation Act of 1973 Each criminal surveillance order, application, inventory, and public docket record for any criminal surveillance case required under this subsection shall be published in a form that complies with section 508 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794d ). (5) Nondisclosure orders When applying for an order for nondisclosure under section 2705, to prevent the disclosure of a subpoena\u2014 (A) the applicant for the order shall include a copy of the subpoena; and (B) the court shall docket the subpoena as part of the application for the order. (6) Automatic unsealing and notification The court shall employ a technical mechanism to automatically\u2014 (A) unseal criminal surveillance orders not later than the end of the next business day after the seal expires; and (B) provide notice, 10 business days before scheduled unsealing, to the law enforcement agency that filed the application for the criminal surveillance order. (c) Filing An application and the inventory shall be filed electronically. 3133. Request for unsealing or challenging redactions (a) In general Any person may submit a request to a court to\u2014 (1) unseal an application for a criminal surveillance order, a criminal surveillance order, or an inventory; or (2) challenge a redaction under section 3132(a)(2)(C)(ii)(II). (b) Form A request described in subsection (a) may be submitted as part of\u2014 (1) the particular criminal surveillance matter, including as a motion to unseal; or (2) as a stand-alone, separate case. (c) Multiple applications and orders unsealed A request described in subsection (a) may include more than 1 application for a criminal surveillance order, criminal surveillance order, or an inventory. .\n##### (b) Technical and conforming amendments\n**(1) In general**\nTitle 18, United States Code, is amended\u2014\n**(A)**\nin section 2518(8)\u2014\n**(i)**\nby striking paragraph (b); and\n**(ii)**\nby redesignating paragraphs (c) and (d) as subparagraphs (b) and (c), respectively;\n**(B)**\nin section 3123, by striking subsection (d); and\n**(C)**\nin section 3103a(b)(1)\u2014\n**(i)**\nby striking 2705 and inserting 3132) ; and\n**(ii)**\nby striking trial) and inserting trial .\n**(2) E-Government Act of 2002**\n**(A) In general**\nSection 205 of the E-Government Act of 2002 ( 44 U.S.C. 3501 note) is amended\u2014\n**(i)**\nin subsection (a), by adding at the end the following:\n(8) Access to the substance of all applications for criminal surveillance orders, criminal surveillance orders, and inventories in a text searchable format in accordance with chapter 206A of title 18, United States Code. ; and\n**(ii)**\nin subsection (c)\u2014\n**(I)**\nby striking paragraph (2) and inserting the following:\n(2) Exceptions (A) In general Documents that are filed that are not otherwise available to the public, such as documents filed under seal, shall not be made available online. (B) Criminal surveillance orders Subparagraph (A) shall not apply to applications for criminal surveillance orders, criminal surveillance orders, and inventories that are publicly available in accordance with chapter 206A of title 18, United States Code. ; and\n**(II)**\nin paragraph (3), by adding at the end the following:\n(D) The Supreme Court shall update the rules prescribed under subparagraph (A) to address personal information included in criminal surveillance orders, applications, and inventories that are made available to the public. .\n**(3) Table of chapters**\nThe table of chapters for part II of title 18, United States Code, is amended by inserting after the item relating to chapter 206 the following:\n206A. Criminal surveillance orders 3121 .\n##### (c) Effective date\n**(1) In general**\nExcept as provided in paragraphs (2) and (3), the amendments made by this section shall take effect on the date that is 2 years after the date of enactment of this Act.\n**(2) Delayed applicability for certain State and Tribal courts**\n**(A) In general**\nSubsections (b)(1)(A) and (c) of section 3132 of title 18, United States Code, as added by subsection (a) of this section, shall apply on and after the date that is 4 years after the date of enactment of this Act\u2014\n**(i)**\nto a State or Tribal court that, on the date of enactment of this Act, does not offer electronic docketing or public online access to dockets; or\n**(ii)**\nany State or Tribal court that certifies that the court needs more time to comply with the requirements of those subsections.\n**(3) Authority to delay electronic filing**\n**(A) Certification**\n**(i) Federal courts**\nThe application of subsection (c) of section 3132 of title 18, United States Code, as added by subsection (a) of this section, to Federal courts under paragraph (1) of this subsection shall be delayed for 1 year if the Director of the Administrative Office of the United States Courts certifies that the system used by Federal courts for electronic filing is not sufficiently secure.\n**(ii) State and Tribal courts**\nThe application of subsection (c) of section 3132 of title 18, United States Code, as added by subsection (a) of this section, to a State or Tribal court under paragraph (1) or (2) of this subsection, as applicable, shall be delayed for 1 year if the chief judge of the highest court of the State or Tribe certifies that the system used by the State or Tribal court for electronic filing is not sufficiently secure.\n**(B) Contents**\nA certification under subparagraph (A) shall include an estimate of the date by which the electronic filing system of the applicable court will be sufficiently secure.\n**(C) Renewal of delay**\nThe delay of the application of subsection (c) of section 3132 of title 18, United States Code, as added by subsection (a) of this section, to Federal courts or to a State or Tribal court may be delayed for 1 or more additional 1-year periods if the Director of the Administrative Office of the United States Courts or the chief judge of the highest court of the State or Tribe, respectively, submits an additional certification in accordance with subparagraphs (A) and (B).\n**(D) Publication**\nAny certification under this paragraph shall be\u2014\n**(i)**\nmade available on the website of the court system with respect to which the certification is submitted; and\n**(ii)**\nsubmitted to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives.\n##### (d) Applicability\n**(1) Definitions**\nIn this subsection, the terms application , criminal surveillance order , and inventory have the meanings given such terms in section 3131 of title 18, United States Code, as added by subsection (a).\n**(2) Application**\nThe amendments made by this section shall apply to\u2014\n**(A)**\nany application filed or inventory returned on or after the date described in subsection (d); and\n**(B)**\nany criminal surveillance order entered on or after the date described in subsection (d).\n**(3) Rule of construction regarding unsealing**\nNothing in the amendments made by this section shall be construed to prohibit a court from unsealing\u2014\n**(A)**\na criminal surveillance order entered or inventory returned before the date described in subsection (d); or\n**(B)**\nan application for a criminal surveillance order made before the date described in subsection (d).\n**(4) Rule of construction regarding interpretation**\nThe amendments made by this section shall be liberally construed in favor of public access to documents, to the extent possible.\n#### 3. Notice to courts of unlawful surveillance\n##### (a) Required disclosure of customer communications or records\nSection 2703(d) of title 18, United States Code, is amended\u2014\n**(1)**\nby striking A court order and inserting the following:\n(1) In general A court order ; and\n**(2)**\nby adding at the end the following:\n(2) Required inventory A court order for disclosure issued under subsection (b) or (c) shall require an inventory described in rule 41(f)(1)(B) of the Federal Rules of Criminal Procedure, or any successor thereto, be promptly returned to the court if the provider disclosed to the government any data not authorized by the court. .\n##### (b) Issuance of an order for a pen register or a trap and trace device\nSection 3123(b) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)(D), by striking and at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) shall require an inventory described in rule 41(f)(1)(B) of the Federal Rules of Criminal Procedure, or any successor thereto, be promptly returned to the court if\u2014 (A) the provider disclosed to the government any electronic data not authorized by the court; or (B) the government obtained dialing, routing, addressing, or signaling information that was not authorized by the court or in a manner that exceeded the authorization granted by the court. .\n##### (c) Rule 41\nRule 41(f)(1)(B) of the Federal Rules of Criminal Procedure is amended by inserting after the period at the end the following:\nIf an inventory is required pursuant to this rule, or if an inventory is required by section 2703(d)(2) of title 18, United States Code, or section 3123(b)(3) of that title, the inventory shall\u2014 (i) disclose whether the provider disclosed to the government any electronic data not authorized by the court and, if so, provide detailed information regarding the disclosure; and (ii) disclose whether the government searched persons or property, including accounts or electronic devices, or obtained dialing, routing, addressing, or signaling information not authorized by the court or in a manner that exceeded the authorization granted by the court and, if so, provide detailed information regarding the search. .\n#### 4. Notice to subjects of law enforcement surveillance\n##### (a) In general\nSection 2703 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), in the first sentence\u2014\n**(A)**\nby inserting and in accordance with the requirements for executing and returning a warrant after the procedures ;\n**(B)**\nby inserting and execution and return after State warrant ; and\n**(C)**\nby inserting and in accordance with the requirements for executing and returning such a warrant after that title ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking without required notice to the subscriber or customer, ;\n**(II)**\nby inserting and in accordance with the requirements for executing and returning a warrant after the procedures ;\n**(III)**\nby inserting and execution and return after State warrant ; and\n**(IV)**\nby inserting and in accordance with the requirements for executing and returning such a warrant after that title ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (ii), by striking the semicolon at the end and inserting a period; and\n**(II)**\nin the matter following clause (ii), by striking except that delayed notice may be given pursuant to section 2705 of this title. ; and\n**(B)**\nby adding at the end the following:\n(3) Notice may not be delayed pursuant to section 2705 for a disclosure under paragraph (1)(B)(i). ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A)\u2014\n**(i)**\nby inserting and in accordance with the requirements for executing and returning a warrant after the procedures ;\n**(ii)**\nby inserting and execution and return after State warrant ; and\n**(iii)**\nby inserting and in accordance with the requirements for executing and returning such a warrant after that title ; and\n**(B)**\nby striking paragraph (3);\n**(4)**\nin subsection (d), as amended by section 3(a) of this Act, by adding at the end the following:\n(3) Requirements Orders under this subsection shall be issued in accordance with the requirements for executing and returning a warrant under the Federal Rules of Criminal Procedure. ; and\n**(5)**\nby adding at the end the following:\n(i) Service (1) In general A governmental entity receiving records or information under subsection (a), (b), or (c) of this section or seeking an order under section 3123 shall provide notice prior to conducting the court-authorized surveillance to the subscriber or customer or the person described in subsection (b)(1)(A) of that section, as applicable, unless notice is delayed in accordance with section 2705. If prior notice is infeasible due to inadequate contact information, the governmental entity shall provide the required notice within 7 days after receipt of adequate contact information from the provider. (2) Other requirements For purposes of serving a copy of a warrant or order described in this section and a receipt for the warrant or order\u2014 (A) the person or persons whose wire or electronic communications are obtained under the warrant or order shall be the person or persons whose property was searched or who possessed the information that was seized or copied; and (B) service of the copy of the warrant or order and the receipt may only be delayed in accordance with section 2705. .\n##### (b) Writs\nSection 1651 of title 28, United States Code, is amended by adding at the end the following:\n(c) In seeking an order to a third party under this section, the Federal Government shall comply with any requirement for notice applicable to warrants issued under the Federal Rules of Criminal Procedure. .\n##### (c) Voluntary disclosure of customer communications or records\nSection 2702 of title 18, United States Code, is amended by adding at the end the following:\n(e) Notice If a governmental entity requests and receives a voluntary disclosure from a provider described in subsection (a)\u2014 (1) the contents of communications pursuant to subsection (b)(8); or (2) a record or other information pertaining to a subscriber to or customer of such service pursuant to subsection (c)(4), the governmental entity shall within 7 days provide notice to the subscriber or customer, unless notice is delayed in accordance with section 2705. .\n#### 5. Delay and preclusion of required notice\n##### (a) In general\nSection 2705 of title 18, United States Code, is amended\u2014\n**(1)**\nin the section heading, by striking Delayed and inserting Delay and preclusion of ;\n**(2)**\nby striking subsection (a) and inserting the following:\n(a) Delay of required notice to customer or subscriber (1) In general A governmental entity acting under section 2702, 2703, or section 3123 may apply to a court for an order delaying the required notice to the person whose wire or electronic communications or records or information are obtained. (2) Warrants and orders The court may enter an order described in paragraph (1) with respect to a warrant or order only if the warrant or order is sealed in accordance with chapter 206A, and only for the period during which the sealing order is in effect. (3) Subpoenas and emergency requests (A) In general The court shall enter an order described in paragraph (1) with respect to a subpoena or emergency request for a period not to exceed 180 days after the return date of the subpoena or the emergency request if the governmental entity certifies that there is reason to believe that failure to issue the order will have an adverse result described in section 3132(a)(2)(B). (B) Extensions (i) In general The court shall grant a single extension of an order described in paragraph (1) with respect to a subpoena or emergency request for a period not to exceed 180 days upon the governmental entity's motion, based on a renewed certification that failure to extend the order will have an adverse result described in section 3132(a)(2)(B). (ii) Subsequent extensions (I) In general For any extension after an extension under clause (i), the court may grant an extension of an order described in paragraph (1) with respect to a subpoena or emergency request for up to 180 days, upon the governmental entity's motion, if the governmental entity demonstrates a particularized showing described in subitems (AA) and (BB) of section 3132(a)(2)(C)(I)(aa) and details the information described in item (bb) of section 3132(a)(2)(C)(I). (II) Redacted documents The court shall consider and order redactions under this clause in accordance with the procedures under section 3132(a)(2)(C)(II). (C) Review by court The court may, in its discretion, require the governmental entity to provide the factual basis for the certification described in subparagraph (A) and may review that factual basis for sufficiency. (D) Notification (i) In general A governmental entity shall promptly notify the court once the governmental entity no longer has reason to believe that the order is necessary to prevent an adverse result described in section 3132(a)(2)(B). (ii) Revocation After being notified by the governmental entity under clause (i), the court shall revoke the order. ; and\n**(3)**\nby adding at the end the following:\n(c) Reports concerning preclusion of notice orders (1) In general In January of each year, any judge who has issued an order (or an extension thereof) under subsection (b) that expired during the preceding year, or who has denied approval of a request for a preclusion of notice order, shall report to the Administrative Office of the United States Courts\u2014 (A) the fact that an order or extension was applied for; (B) the fact that the order or extension was granted as applied for, was modified, or was denied; (C) the period of the preclusion of notice required by the order, and the number and duration of any extensions of the order; (D) the nature of the offense or criminal investigation that was the basis for the underlying criminal surveillance order; (E) the name of each provider of electronic communication service or remote computing service served with the order, if so granted; and (F) the investigative or law enforcement agency that submitted the application. (2) Public report In June of each year, the Director of the Administrative Office of the United States Courts shall publish on the website of the Administrative Office of the United States Courts and include in the report required under section 2519(3)\u2014 (A) a full and complete report concerning\u2014 (i) the number of applications for orders authorizing or approving the preclusion of notice pursuant to this section; and (ii) the number of orders and extensions granted or denied pursuant to this section during the preceding calendar year; and (B) a detailed summary and analysis of each category of data required to be reported under paragraph (1). (3) Format Not later than 180 days after the date of enactment of this section, the Director of the Administrative Office of the United States Courts shall, in consultation with the National Institute of Standards and Technology and the Administrator of General Services, private entities offering electronic case management software, the National Center for State Courts, and the National American Indian Court Judges Association, publish a machine readable form that shall be used for any report required under paragraph (1). (4) Regulations The Director of the Administrative Office of the United States Courts may promulgate regulations with respect to the content and form of the reports required under paragraph (1). (d) Duration Any order issued under subsection (a) before the effective date of chapter 206A shall be for a period of not longer than 180 days. .\n##### (b) Additional grounds for issuing warrant\nSection 3103a of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(3), by inserting , not to exceed 180 days, after certain ;\n**(2)**\nin subsection (c), by inserting , not to exceed 180 days before the period at the end; and\n**(3)**\nin subsection (d)(1)\u2014\n**(A)**\nin subparagraph (C), by striking and at the end;\n**(B)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) the identification of the statute or rule of law authorizing the search and seizure of property or material. .\n##### (c) Technical and conforming amendment\nThe table of sections for chapter 121 of title 18, United States Code, is amended by striking the item relating to section 2705 and inserting the following:\n2705. Delay and preclusion of notice. .\n#### 6. Incentives for State and Tribal courts to implement requirements\n##### (a) Amendments\n**(1) Stored communications**\nChapter 121 of title 18, United States Code, is amended\u2014\n**(A)**\nin section 2703, as amended by section 4(a) of this Act, by inserting after return procedures each place the term appears the following: and containing a certification that the court is acting in compliance with chapter 206A ; and\n**(B)**\nin section 2711(3)(B), by inserting that is acting in compliance with chapter 206A after search warrants .\n**(2) Wiretapping**\nSection 2516(2) of title 18, United States Code, is amended by striking The principal prosecuting attorney of any State and inserting If a State requires that courts in the state comply with chapter 206A, the principal prosecuting attorney of that State .\n**(3) Pen registers and trap and trace devices**\nSection 3122(a)(2) of title 18, United States Code, is amended by inserting and if the State requires that courts in the state comply with chapter 206A, after law, .\n**(4) Full faith and credit**\nThe third undesignated paragraph of section 1738 of title 28, United States Code, is amended by inserting , provided that any criminal surveillance order, as defined in section 3131 of title 18, shall be entitled to full faith and credit only if the order contains a certification that the court that issued the order is acting in compliance with the requirements of chapter 206A of title 18 before the period at the end.\n##### (b) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by subsection (a) shall take effect on the date that is 2 years after the date of enactment of this Act.\n**(2) Delayed applicability for certain State and Tribal courts**\nThe amendments made by subsection (a) shall apply on and after the date that is 4 years after the date of enactment of this Act\u2014\n**(A)**\nto a State or Tribal court that, on the date of enactment of this Act, does not offer electronic docketing or public online access to dockets; or\n**(B)**\nto any State or Tribal court that certifies that the court needs more time to comply with the requirements of the subsection.\n#### 7. Modernizing criminal surveillance reports\n##### (a) Reports concerning access to customer communications or records\n**(1) In general**\nSection 2703 title 18, United States Code, as amended by section 4(5) of this Act, is amended by adding at the end the following:\n(j) Reports concerning access to customer communications or records (1) In general In January of each year, any judge who has issued an order under this section or a warrant to obtain records described in this section, or who has denied approval of an application under this section during the preceding year, shall report to the Administrative Office of the United States Courts\u2014 (A) the fact that the order or warrant was applied for; (B) the type of records sought in the order or warrant; (C) whether the order or warrant was\u2014 (i) granted as applied for; (ii) granted as modified; or (iii) denied; (D) the subsection of this section under which the application for the order or warrant was filed; (E) the nature of the offense or criminal investigation that was the basis for the application for the order or warrant; (F) the name of each provider of electronic communication service or remote computing service served with the order or warrant, if so granted; and (G) the investigative or law enforcement agency that submitted the application. (2) Public report In June of each year, the Director of the Administrative Office of the United States Courts shall publish on the website of the Administrative Office of the United States Courts and include in the report required under section 2519(3)\u2014 (A) a full and complete report concerning the number of applications for orders or warrants requiring the disclosure of, during the preceding calendar year\u2014 (i) the contents of wire or electronic communications in electronic storage under subsection (a); (ii) the contents of wire or electronic communications in a remote computer service under subsection (b); and (iii) records concerning electronic communication service or remote computer service under subsection (c); (B) the number of orders and warrants granted or denied under this section during the preceding calendar year; and (C) a detailed summary and analysis of each category of data required to be filed with the Administrative Office of the United States Courts under paragraph (1). (3) Format Not later than 180 days after the date of enactment of the Government Surveillance Transparency Act of 2026 , the Director of the Administrative Office of the United States Courts shall, in consultation with the National Institute of Standards and Technology, the Administrator of General Services, the Electronic Public Access Public User Group, private entities offering electronic case management software, the National Center for State Courts, and the National American Indian Court Judges Association, publish a machine readable form that shall be used for any report required under paragraph (1). (4) Regulations The Director of the Administrative Office of the United States Courts may issue binding regulations with respect to the content and form of the reports required under paragraph (1). .\n**(2) Technical and conforming amendment**\nSection 2519(3) of title 18, United States Code, is amended, in the first sentence, by inserting publish on the website of the Administrative Office of the United States Courts before transmit .\n##### (b) Reports concerning pen registers and trap and trace devices\nSection 3126 of title 18, United States Code, is amended to read as follows:\n3126. Reports concerning pen registers and trap and trace devices (a) In general In January of each year, any judge who has issued an order (or an extension thereof) under section 3123 that expired during the preceding year, or who has denied approval of an installation and use of a pen register or trap and trace device during that year, shall report to the Administrative Office of the United States Courts\u2014 (1) the fact that an order or extension was applied for; (2) the kind of order or extension applied for; (3) the fact that the order or extension was granted as applied for, was modified, or was denied; (4) the period of installation and use of a pen register or trap and trace device authorized by the order, and the number and duration of any extensions of the order; (5) the offense specified in the order or application, or extension of an order; (6) the precise nature of the facilities affected and the precise nature of the information sought; and (7) the investigative or law enforcement agency that submitted the application. (b) Public report In June of each year, the Director of the Administrative Office of the United States Courts shall publish on the website of the Administrative Office of the United States Courts and include in the report required under section 2519(3)\u2014 (1) a full and complete report concerning\u2014 (A) the number of applications for orders authorizing or approving the installation and use of a pen register or trap and trace device pursuant to this chapter; and (B) the number of orders and extensions granted or denied pursuant to this chapter during the preceding calendar year; and (2) a detailed summary and analysis of each category of data required to be reported under subsection (a). (c) Format Not later than 180 days after the date of enactment of the Government Surveillance Transparency Act of 2026 , the Director of the Administrative Office of the United States Courts shall, in consultation with the National Institute of Standards and Technology and the Administrator of General Services, private entities offering electronic case management software, the National Center for State Courts, and the National American Indian Court Judges Association, publish a machine readable form that shall be used for any report required under subsection (a). (d) Regulations The Director of the Administrative Office of the United States Courts may issue binding regulations with respect to the content and form of the reports required under subsection (a). .\n##### (c) Reporting of emergency disclosures\nSection 2702(d) of title 18, United States Code, is amended, in the matter preceding paragraph (1), by inserting and publish on the website of the Department of Justice after Senate .\n#### 8. Grants\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term Indian Tribe has the meaning given such term in section 102 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130 ); and\n**(2)**\nthe term State means each of the several States of the United States, the District of Columbia, the Commonwealth of Puerto Rico, American Samoa, the Commonwealth of the Northern Mariana Islands, Guam, and the United States Virgin Islands.\n##### (b) Authority\nThe Attorney General shall make grants to State and Tribal court systems for the cost of implementing the requirements under the amendments made by this Act for the 5-year period beginning on the date of enactment of this Act.\n##### (c) Maximum amount\nThe total amount of grants awarded under this section shall be not greater than $25,000,000.\n#### 9. Authorization of appropriations\nThere are authorized to be appropriated\u2014\n**(1)**\n$1,000,000 to the Administrative Office of the United States Courts to implement the requirements of this Act and the amendments made by this Act; and\n**(2)**\n$25,000,000 to carry out the grant program under section 8.\n#### 10. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any person or circumstance, is held to be unconstitutional, the remaining provisions of and amendments made by this Act, and the application of the provision or amendment held to be unconstitutional to any other person or circumstance, shall not be affected thereby.",
      "versionDate": "2026-02-25",
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
        "actionDate": "2026-02-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7738",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Government Surveillance Transparency Act of 2026",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-16T15:21:40Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3918is.xml"
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
      "title": "Government Surveillance Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Government Surveillance Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to require that notice of criminal surveillance orders be eventually provided to targets, to reform the use of non-disclosure orders to providers, to prohibit indefinite sealing of criminal surveillance orders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T03:49:24Z"
    }
  ]
}
```
