# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3998?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3998
- Title: PIONEER Act
- Congress: 119
- Bill type: S
- Bill number: 3998
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-30T22:27:10Z
- Update date including text: 2026-03-30T22:27:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3998",
    "number": "3998",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "PIONEER Act",
    "type": "S",
    "updateDate": "2026-03-30T22:27:10Z",
    "updateDateIncludingText": "2026-03-30T22:27:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:57:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3998is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3998\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish a regulatory sandbox program under which agencies may provide waivers of agency rules and guidance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Innovation and Offering the Needed Escape from Exhaustive Regulations Act or the PIONEER Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Office of Information and Regulatory Affairs.\n**(2) Agency; rule**\nThe terms agency and rule have the meanings given those terms in section 551 of title 5, United States Code.\n**(3) Applicable agency**\nThe term applicable agency means an agency that has jurisdiction over the enforcement or implementation covered provision for which an applicant is seeking a waiver under the Program.\n**(4) Covered provision**\nThe term covered provision means\u2014\n**(A)**\na rule, including a rule required to be issued under law; or\n**(B)**\nguidance or any other document issued by an agency.\n**(5) Director**\nThe term Director means the Director of the Office.\n**(6) Economic damage**\nThe term economic damage means a risk that is likely to cause tangible, physical harm to the property or assets of consumers.\n**(7) Health or safety**\nThe term health or safety , with respect to a risk, means the risk is likely to cause bodily harm to a human life, loss of human life, or an inability to sustain the health or life of a human being.\n**(8) Office**\nThe term Office means the Office of Federal Regulatory Relief established under section 3(a).\n**(9) Program**\nThe term Program means the program established under section 4(a).\n**(10) Unfair or deceptive trade practice**\nThe term unfair or deceptive trade practice has the meaning given the term in\u2014\n**(A)**\nthe Policy Statement of the Federal Trade Commission on Deception, issued on October 14, 1983; and\n**(B)**\nthe Policy Statement of the Federal Trade Commission on Unfairness, issued on December 17, 1980.\n#### 3. Office of Federal Regulatory Relief\n##### (a) Establishment\nThere is established within the Office of Information and Regulatory Affairs within the Office of Management and Budget an Office of Federal Regulatory Relief.\n##### (b) Director\n**(1) In general**\nThe Office shall be headed by a Director, who shall be the Administrator or a designee thereof, who shall\u2014\n**(A)**\nbe responsible for\u2014\n**(i)**\nestablishing a regulatory sandbox program described in section 4;\n**(ii)**\nreceiving Program applications and ensuring those applications are complete;\n**(iii)**\nreferring complete Program applications to the applicable agencies;\n**(iv)**\nfiling final Program application decisions from the applicable agencies;\n**(v)**\nhearing appeals from applicants if their applications are denied by an applicable agency in accordance with section 4(c)(8); and\n**(vi)**\ndesignating staff to the Office as needed; and\n**(B)**\nnot later than 180 days after the date of enactment of this Act\u2014\n**(i)**\nestablish a process that is used to assess likely health and safety risks, risks that are likely to cause economic damage, and the likelihood for unfair or deceptive practices to be committed against consumers related to applications submitted for the Program, which shall be\u2014\n**(I)**\npublished in the Federal Register and made publicly available with a detailed list of the criteria used to make such determinations; and\n**(II)**\nsubject to public comment before final publication in the Federal Register; and\n**(ii)**\nestablish the application process described in section 4(c)(1).\n**(2) Advisory boards**\n**(A) Establishment**\nThe Director shall require the head of each agency to establish an advisory board, which shall\u2014\n**(i)**\nbe composed of 10 private sector representatives appointed by the head of the agency\u2014\n**(I)**\nwith expertise in matters under the jurisdiction of the agency, with not more than 5 representatives from the same political party;\n**(II)**\nwho shall serve for a period of not more than 3 years; and\n**(III)**\nwho shall not receive any compensation for participation on the advisory board; and\n**(ii)**\nbe responsible for providing input to the head of the agency for each Program application received by the agency.\n**(B) Vacancy**\nA vacancy on an advisory board established under subparagraph (A), including a temporary vacancy due to a recusal under subparagraph (C)(ii), shall be filled in the same manner as the original appointment with an individual who meets the qualifications described in subparagraph (A)(i)(I).\n**(C) Conflict of interest**\n**(i) In general**\nIf a member of an advisory board established under subparagraph (A) is also the member of the board of an applicant that submits an application under review by the advisory board, the head of the agency or a designee thereof may appoint a temporary replacement for that member.\n**(ii) Financial interest**\nEach member of an advisory board established under subparagraph (A) shall recuse themselves from advising on an application submitted under the Program for which the member has a conflict of interest as described in section 208 of title 18, United States Code.\n**(D) Small business concerns**\nNot less than 5 of the members of each advisory board established under subparagraph (A) shall be representatives of a small business concern, as defined in section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n**(E) Rule of construction**\nNothing in this Act shall be construed to prevent an agency from establishing additional advisory boards as needed to assist in reviewing Program applications that involve multiple or unique industries.\n#### 4. Regulatory sandbox program\n##### (a) In general\nThe Director shall establish a regulatory sandbox program under which applicable agencies shall grant or deny waivers of covered provisions to temporarily test products or services on a limited basis, or undertake a project to expand or grow business facilities consistent with the purpose described in subsection (b), without otherwise being licensed or authorized to do so under that covered provision.\n##### (b) Purpose\nThe purpose of the Program is to incentivize the success of current or new businesses, the expansion of economic opportunities, the creation of jobs, and the fostering of innovation.\n##### (c) Application process for waivers\n**(1) In general**\nThe Office shall establish an application process for the waiver of covered provisions, which shall require that an application shall\u2014\n**(A)**\nconfirm that the applicant\u2014\n**(i)**\nis subject to the jurisdiction of the Federal Government; and\n**(ii)**\nhas established or plans to establish a business that is incorporated or has a principal place of business in the United States from which their goods or services are offered from and their required documents and data are maintained;\n**(B)**\ninclude relevant personal information such as the legal name, address, telephone number, email address, and website address of the applicant;\n**(C)**\ndisclose any criminal conviction of the applicant or other participating persons, if applicable;\n**(D)**\ncontain a description of the good, service, or project to be offered by the applicant for which the applicant is requesting waiver of a covered provision by the Office under the Program, including\u2014\n**(i)**\nhow the applicant is subject to licensing, prohibitions, or other authorization requirements outside of the Program;\n**(ii)**\neach covered provision that the applicant seeks to have waived during participation in the Program;\n**(iii)**\nhow the good, service, or project would benefit consumers;\n**(iv)**\nwhat likely risks the participation of the applicant in the Program may pose, and how the applicant intends to reasonably mitigate those risks;\n**(v)**\nhow participation in the Program would render the offering of the good, service, or project successful;\n**(vi)**\na description of the plan and estimated time periods for the beginning and end of the offering of the good, service, or project under the Program;\n**(vii)**\na recognition that the applicant will be subject to all laws and rules after the conclusion of the offering of the good, service, or project under the Program;\n**(viii)**\nhow the applicant will end the demonstration of the offering of the good, service, or project under the Program;\n**(ix)**\nhow the applicant will repair harm to consumers if the offering of the good, service, or project under the Program fails; and\n**(x)**\na list of each agency that regulates the business of the applicant; and\n**(E)**\ninclude any other information as required by the Office.\n**(2) Assistance**\nThe Office may, upon request, provide assistance to an applicant to complete the application process for a waiver under the Program, including by providing the likely covered provisions that could be eligible for such a waiver.\n**(3) Agency review**\n**(A) Transmission**\nNot later than 14 days after the date on which the Office receives an application under paragraph (1), the Office shall submit a copy of the application to each applicable agency.\n**(B) Review**\nThe head of an applicable agency, or a designee thereof, shall review a Program application received under subparagraph (A) with input from the advisory board established under section 3(b)(2).\n**(C) Considerations**\nIn reviewing a copy of an application submitted to an applicable agency under subparagraph (A), the head of the applicable agency, or a designee thereof, with input from the advisory board of the applicable agency established under section 3(b)(2), shall consider whether\u2014\n**(i)**\nthe plan of the applicant to deploy their offering will adequately protect consumers from harm;\n**(ii)**\nthe likely health and safety risks, risks that are likely to cause economic damage, and the likelihood for unfair or deceptive practices to be committed against consumers are outweighed by the potential benefits to consumers from the offering of the applicant; and\n**(iii)**\nit is possible to provide the applicant a waiver even if the Office does not waive every covered provision requested by the applicant.\n**(D) Final decision**\n**(i) In general**\nSubject to clause (ii), the head of an applicable agency, or a designee thereof, who receives a copy of an application under subparagraph (A) shall, with the consideration of the recommendations of the advisory board of the applicable agency established under section 3(b)(2), make the final decision to grant or deny the application.\n**(ii) In part approval**\n**(I) In general**\nIf more than 1 applicable agency receives a copy of an application under subparagraph (A)\u2014\n**(aa)**\nthe head of each applicable agency (or their designees), with input from the advisory board of the applicable agency established under section 3(b)(2), shall grant or deny the waiver of the covered provisions over which the applicable agency has jurisdiction for enforcement or implementation; and\n**(bb)**\nif each applicable agency that receives an application under subparagraph (A) grants the waiver under item (aa), the Director shall grant the entire application.\n**(II) In part approval by Director**\nIf an applicable agency denies part of an application under subclause (I) but another applicable agency grants part of the application, the Director shall approve the application in part and specify in the final decision which covered provisions are waived.\n**(E) Record of decision**\n**(i) In general**\nNot later than 180 days after receiving a copy of an application under subparagraph (A), an applicable agency shall approve or deny the application and submit to the Director a record of the decision, which shall include a description of each likely health and safety risk, each risk that is likely to cause economic damage, and the likelihood for unfair or deceptive practices to be committed against consumers that the covered provision the applicant is seeking to have waived protects against, and\u2014\n**(I)**\nif the application is approved, a description of how the identifiable, significant harms will be mitigated and how consumers will be protected under the waiver;\n**(II)**\nif the applicable agency denies the waiver, a description of the reasons for the decision, including why a waiver would likely cause health and safety risks, likely cause economic damage, and increase the likelihood for unfair or deceptive practices to be committed against consumers, and the likelihood of such risks occurring, as well as reasons why the application cannot be approved in part or reformed to mitigate such risks; and\n**(III)**\nif the applicable agency determines that a waiver would likely cause health and safety risks, likely cause economic damage, and there is likelihood for unfair or deceptive practices to be committed against consumers as a result of the covered provision that an applicant is requesting to have waived, but the applicable agency determines such risks can be protected through less restrictive means than denying the application, the applicable agency shall provide a recommendation of how that can be achieved.\n**(ii) No record submitted**\nIf the applicable agency does not submit a record of the decision with respect to an application for a waiver submitted to the applicable agency, the Office shall assume that the applicable agency does not object to the granting of the waiver.\n**(iii) Extension**\nThe applicable agency may request one 30-day extension of the deadline for a record of decision under clause (i).\n**(iv) Expedited review**\nIf the applicable agency provides a recommendation described in clause (i)(III), the Office shall provide the applicant with a 60-day period to make necessary changes to the application, and the applicant may resubmit the application to the applicable agency for expedited review over a period of not more than 60 days.\n**(4) Nondiscrimination**\nIn considering an application for a waiver, an applicable agency shall not unreasonably discriminate among applications under the Program or resort to any unfair or unjust discrimination for any reason.\n**(5) Fee**\nThe Office may collect an application fee from each applicant under the Program, which\u2014\n**(A)**\nshall be in a fair amount and reflect the cost of the service provided;\n**(B)**\nshall be deposited in the general fund of the Treasury and allocated to the Office, subject to appropriations; and\n**(C)**\nshall not be increased more frequently than once every 2 years.\n**(6) Written agreement**\nIf each applicable agency grants a waiver requested in an application submitted under paragraph (1), the waiver shall not be effective until the applicant enters into a written agreement with the Office that describes each covered provision that is waived under the Program.\n**(7) Limitation**\nAn applicable agency may not waive under the Program any tax, fee, or charge imposed by the Federal Government.\n**(8) Appeals**\n**(A) In general**\nIf an applicable agency denies an application under paragraph (3)(E), the applicant may submit to the Office one appeal for reconsideration, which shall\u2014\n**(i)**\naddress the comments of the applicable agency that resulted in denial of the application; and\n**(ii)**\ninclude how the applicant plans to mitigate the likely risks identified by the applicable agency.\n**(B) Office response**\nNot later than 60 days after receiving an appeal under subparagraph (A), the Director shall\u2014\n**(i)**\ndetermine whether the appeal sufficiently addresses the concerns of the applicable agency; and\n**(ii)**\n**(I)**\nif the Director determines that the appeal sufficiently addresses the concerns of the applicable agency, file a record of decision detailing how the concerns have been remedied and approve the application; or\n**(II)**\nif the Director determines that the appeal does not sufficiently address the concerns of the applicable agency, file a record of decision detailing how the concerns have not been remedied and deny the application.\n**(9) Nondiscrimination**\nThe Office shall not unreasonably discriminate among applications under the Program or resort to any unfair or unjust discrimination for any reason in the implementation of the Program.\n**(10) Judicial review**\n**(A) Record of decision**\nA record of decision described in paragraph (3)(E) or (8)(B) shall be considered a final agency action for purposes of review under section 704 of title 5, United States Code.\n**(B) Limitation**\nA reviewing court considering claims made against a final agency action under this Act shall be limited to whether the agency acted in accordance with the requirements set forth under this Act.\n**(C) Right to judicial review**\nNothing in this paragraph shall be construed to establish a right to judicial review under this Act.\n##### (d) Period of waiver\n**(1) Initial period**\nExcept as provided in this subsection, a waiver granted under the Program shall be for a term of 2 years.\n**(2) Continuance**\nThe Office may continue a waiver granted under the Program for a maximum of 4 additional periods of 2 years as determined by the Office.\n**(3) Notification**\nNot later than 30 days before the end of an initial waiver period under paragraph (1), an entity that is granted a waiver under the Program shall notify the Office if the entity intends to seek a continuance under paragraph (2).\n**(4) Revocation**\n**(A) Significant harm**\nIf the Office determines that an entity that was granted a waiver under the Program is causing significant harm to the health or safety of the public, inflicting severe economic damage on the public, or engaging in unfair or deceptive practices, the Office may immediately end the participation of the entity in the Program by revoking the waiver.\n**(B) Compliance**\nIf the Office determines that an entity that was granted a waiver under the Program is not in compliance with the terms of the Program, the Office shall give the entity 30 days to correct the action, and if the entity does not correct the action by the end of the 30-day period, the Office may end the participation of the entity in the Program by revoking the waiver.\n##### (e) Terms\nAn entity for which a waiver is granted under the Program shall be subject to the following terms:\n**(1)**\nA covered provision may not be waived if the waiver would prevent a consumer from seeking actual damages or an equitable remedy in the event that a consumer is harmed.\n**(2)**\nWhile a waiver is in use, the entity shall not be subject to the criminal or civil enforcement of a covered provision identified in the waiver.\n**(3)**\nAn agency may not file or pursue any punitive action against a participant during the period for which the waiver is in effect, including a fine or license suspension or revocation for the violation of a covered provision identified in the waiver.\n**(4)**\nThe entity shall not have immunity related to any criminal offense committed during the period for which the waiver is in effect.\n**(5)**\nThe Federal Government shall not be responsible for any business losses or the recouping of application fees if the waiver is denied or the waiver is revoked at any time.\n##### (f) Consumer protection\n**(1) In general**\nBefore distributing an offering to consumers under a waiver granted under the Program, and throughout the duration of the waiver, an entity shall publicly disclose the following to consumers:\n**(A)**\nThe name and contact information of the entity.\n**(B)**\nThat the entity has been granted a waiver under the Program, and if applicable, that the entity does not have a license or other authorization to provide an offering under covered provisions outside of the waiver.\n**(C)**\nIf applicable, that the offering is undergoing testing and may not function as intended and may expose the consumer to certain risks as identified in the record of decision of the applicable agency submitted under section 4(c)(3)(E).\n**(D)**\nThat the entity is not immune from civil liability for any losses or damages caused by the offering.\n**(E)**\nThat the entity is not immune from criminal prosecution for violation of covered provisions that are not suspended under the waiver.\n**(F)**\nThat the offering is a temporary demonstration and may be discontinued at the end of the initial period under subsection (d)(1).\n**(G)**\nThe expected commencement date of the initial period under subsection (d)(1).\n**(H)**\nThe contact information of the Office and that the consumer may contact the Office and file a complaint.\n**(2) Online offering**\nWith respect to an offering provided over the internet under the Program, the consumer shall acknowledge receipt of the disclosures required under paragraph (1) before any transaction is completed.\n##### (g) Record keeping\n**(1) In general**\nAn entity that is granted a waiver under this section shall retain records, documents, and data produced that is directly related to the participation of the entity in the Program.\n**(2) Notification before ending offering**\nIf an applicant decides to end their offering before the initial period ends under subsection (d)(1), the applicant shall submit to the Office and the applicable agency a report on actions taken to ensure consumers have not been harmed as a result.\n**(3) Request for documents**\nThe Office may request records, documents, and data from an entity that is granted a waiver under this section that is directly related to the participation of the entity in the Program, and upon the request, the applicant shall make such records, documents, and data available for inspection by the Office.\n**(4) Notification of incidents**\nAn entity that is granted a waiver under this section shall notify the Office and any applicable agency of any incident that results in harm to the health or safety of consumers, severe economic damage, or an unfair or deceptive practice under the Program not later than 72 hours after the incident occurs.\n##### (h) Reports\n**(1) Entities granted a waiver**\n**(A) In general**\nAny entity that is granted a waiver under this section shall submit to the Office reports that include\u2014\n**(i)**\nhow many consumers are participating in the good, service, or project offered by the entity under the Program;\n**(ii)**\nan assessment of the likely risks and how mitigation is taking place;\n**(iii)**\nany previously unrealized risks that have manifested; and\n**(iv)**\na description of any adverse incidents and the ensuing process taken to repair any harm done to consumers.\n**(B) Timing**\nAn entity shall submit a report required under subparagraph (A)\u2014\n**(i)**\n10 days after 30 days elapses from commencement of the period for which a waiver is granted under the Program;\n**(ii)**\n30 days after the halfway mark of the period described in clause (i); and\n**(iii)**\n30 days before the expiration of the period described in subsection (d)(1).\n**(2) Annual report by Director**\nThe Director shall submit to Congress an annual report on the Program, which shall include, for the year covered by the report\u2014\n**(A)**\nthe number of applications approved;\n**(B)**\nthe name and description of each entity that was granted a waiver under the Program;\n**(C)**\nany benefits realized to the public from the Program; and\n**(D)**\nany harms realized to the public from the Program.\n##### (i) Special message to Congress\n**(1) Definition**\nIn this subsection, the term covered resolution means a joint resolution\u2014\n**(A)**\nthe matter after the resolving clause of which contains only\u2014\n**(i)**\na list of some or all of the covered provisions that were recommended for repeal under paragraph (2)(A)(ii) in a special message submitted to Congress under that paragraph; and\n**(ii)**\na provision that immediately repeals the listed covered provisions described in paragraph (2)(A)(ii) upon enactment of the joint resolution; and\n**(B)**\nupon which Congress completes action before the end of the first period of 60 calendar days after the date on which the special message described in subparagraph (A)(i) of this paragraph is received by Congress.\n**(2) Submission**\n**(A) In general**\nNot later than the first day on which both Houses of Congress are in session after May 1 of each year, the Director shall submit to Congress a special message that\u2014\n**(i)**\ndetails each covered provision that the Office recommends should be amended or repealed as a result of entities being able to operate safely without those covered provisions during the Program;\n**(ii)**\nlists any covered provision that should be repealed as a result of having been waived for a period of not less than 6 years during the Program; and\n**(iii)**\nexplains why each covered provision described in clauses (i) and (ii) should be amended or repealed.\n**(B) Delivery to House and Senate; printing**\nEach special message submitted under subparagraph (A) shall be\u2014\n**(i)**\ndelivered to the Clerk of the House of Representatives and the Secretary of the Senate; and\n**(ii)**\nprinted in the Congressional Record.\n**(3) Procedure in House and Senate**\n**(A) Referral**\nA covered resolution shall be referred to the appropriate committee of the House of Representatives or the Senate, as the case may be.\n**(B) Discharge of committee**\nIf the committee to which a covered resolution has been referred has not reported the resolution at the end of 25 calendar days after the introduction of the resolution\u2014\n**(i)**\nthe committee shall be discharged from further consideration of the resolution; and\n**(ii)**\nthe resolution shall be placed on the appropriate calendar.\n**(4) Floor consideration in the House**\n**(A) Motion to proceed**\n**(i) In general**\nWhen the committee of the House of Representatives has reported, or has been discharged from further consideration of, a covered resolution, it shall at any time thereafter be in order (even though a previous motion to the same effect has been disagreed to) to move to proceed to the consideration of the resolution.\n**(ii) Privilege**\nA motion described in clause (i) shall be highly privileged and not debatable.\n**(iii) No amendment or motion to reconsider**\nAn amendment to a motion described in clause (i) shall not be in order, nor shall it be in order to move to reconsider the vote by which the motion is agreed to or disagreed to.\n**(B) Debate**\n**(i) In general**\nDebate in the House of Representatives on a covered resolution shall be limited to not more than 2 hours, which shall be divided equally between those favoring and those opposing the resolution.\n**(ii) No motion to reconsider**\nIt shall not be in order in the House of Representatives to move to reconsider the vote by which a covered resolution is agreed to or disagreed to.\n**(C) No motion to postpone consideration or proceed to consideration of other business**\nIn the House of Representatives, motions to postpone, made with respect to the consideration of a covered resolution, and motions to proceed to the consideration of other business, shall not be in order.\n**(D) Appeals from decisions of chair**\nAn appeal from the decision of the Chair relating to the application of the Rules of the House of Representatives to the procedure relating to a covered resolution shall be decided without debate.\n**(5) Floor consideration in the Senate**\n**(A) Motion to proceed**\n**(i) In general**\nNotwithstanding Rule XXII of the Standing Rules of the Senate, when the committee of the Senate to which a covered resolution is referred has reported, or has been discharged from further consideration of, a covered resolution, it shall at any time thereafter be in order (even though a previous motion to the same effect has been disagreed to) to move to proceed to the consideration of the resolution and all points of order against the covered resolution are waived.\n**(ii) Division of time**\nA motion to proceed described in clause (i) is subject to 4 hours of debate divided equally between those favoring and those opposing the covered resolution.\n**(iii) No amendment or motion to postpone or proceed to other business**\nA motion to proceed described in clause (i) is not subject to\u2014\n**(I)**\namendment;\n**(II)**\na motion to postpone; or\n**(III)**\na motion to proceed to the consideration of other business.\n**(B) Floor consideration**\n**(i) General**\nIn the Senate, a covered resolution shall be subject to 10 hours of debate divided equally between those favoring and those opposing the covered resolution.\n**(ii) Amendments**\nIn the Senate, no amendment to a covered resolution shall be in order, except an amendment that strikes from or adds to the list required under paragraph (1)(A)(i) a covered provision recommended for amendment or repeal by the Office.\n**(iii) Motions and appeals**\nIn the Senate, a motion to reconsider a vote on final passage of a covered resolution shall not be in order, and points of order, including questions of relevancy, and appeals from the decision of the Presiding Officer, shall be decided without debate.\n**(6) Receipt of resolution from other House**\nIf, before passing a covered resolution, one House receives from the other a covered resolution\u2014\n**(A)**\nthe covered resolution of the other House shall not be referred to a committee and shall be deemed to have been discharged from committee on the day on which it is received; and\n**(B)**\nthe procedures set forth in paragraph (4) or (5), as applicable, shall apply in the receiving House to the covered resolution received from the other House to the same extent as those procedures apply to a covered resolution of the receiving House.\n**(7) Rules of the House of representatives and the Senate**\nParagraphs (2) through (6) are enacted by Congress\u2014\n**(A)**\nas an exercise of the rulemaking power of the House of Representatives and the Senate, respectively, and as such are deemed a part of the rules of each House, respectively, but applicable only with respect to the procedures to be followed in the House in the case of covered resolutions, and supersede other rules only to the extent that they are inconsistent with such other rules; and\n**(B)**\nwith full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House.\n##### (j) Rule of construction\nNothing in this section shall be construed to\u2014\n**(1)**\nrequire an entity that is granted a waiver under this section to publicly disclose proprietary information, including trade secrets or commercial or financial information that is privileged or confidential; or\n**(2)**\naffect any other provision of law or regulation applicable to an entity that is not included in a waiver provided under this section.\n##### (k) Authorization of appropriations\nThere are authorized to be appropriated to the Office to carry out this section an amount that is not more than the amount of funds deposited into the Treasury from the fees collected under subsection (c)(5).",
      "versionDate": "2026-03-05",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-30T22:27:09Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3998is.xml"
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
      "title": "PIONEER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T01:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PIONEER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T01:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Innovation and Offering the Needed Escape from Exhaustive Regulations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T01:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a regulatory sandbox program under which agencies may provide waivers of agency rules and guidance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T01:48:19Z"
    }
  ]
}
```
