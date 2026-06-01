# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7220?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7220
- Title: COINTELPRO Full Disclosure Act
- Congress: 119
- Bill type: HR
- Bill number: 7220
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-05-05T08:06:06Z
- Update date including text: 2026-05-05T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-22 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-22 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7220",
    "number": "7220",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000602",
        "district": "12",
        "firstName": "Summer",
        "fullName": "Rep. Lee, Summer L. [D-PA-12]",
        "lastName": "Lee",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "COINTELPRO Full Disclosure Act",
    "type": "HR",
    "updateDate": "2026-05-05T08:06:06Z",
    "updateDateIncludingText": "2026-05-05T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-22T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MI"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7220ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7220\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Ms. Lee of Pennsylvania (for herself and Mr. Jackson of Illinois ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the public disclosure of COINTELPRO records, to establish a COINTELPRO Records Collection, and to establish the COINTELPRO Records Review Board, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the COINTELPRO Full Disclosure Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Public disclosure of COINTELPRO records.\nSec. 3. COINTELPRO Records Collection at the National Archives.\nSec. 4. Establishment and powers of the COINTELPRO Records Review Board.\nSec. 5. COINTELPRO Records Review Board personnel.\nSec. 6. Review of records by the COINTELPRO Records Review Board.\nSec. 7. Disclosure of other information and additional study.\nSec. 8. Rules of construction.\nSec. 9. Redesignation.\nSec. 10. References.\nSec. 11. Funding.\nSec. 12. Definitions.\n#### 2. Public disclosure of COINTELPRO records\n##### (a) In general\nExcept as provided in subsection (b), not later than 6 months after the date of the enactment of this Act, the head of a Government Office shall fully disclose to the public each COINTELPRO record in the possession or control of the Government Office.\n##### (b) Exception\nThe requirement under subsection (a) shall not apply to a COINTELPRO record if the head of the Government Office determines that the full disclosure of such record, or particular information within such record, would clearly and demonstrably be expected to cause harm.\n##### (c) Partial disclosure\nIf the head of a Government Office determines in accordance with subsection (b) that the requirements of subsection (a) do not apply with respect to a COINTELPRO record, the head of the Government Office shall disclose to the public in consultation with the originating body, and to the extent doing so would not clearly and demonstrably be expected to cause harm\u2014\n**(1)**\nany reasonably segregable particular information in a COINTELPRO record;\n**(2)**\na substitute record for that information; or\n**(3)**\na summary of the COINTELPRO record.\n##### (d) Review by Board\nIf a Government Office determines that the requirements of subsection (a) do not apply with respect to a COINTELPRO record, such record shall be transmitted to the Review Board for review in accordance with section 4(b).\n##### (e) Full disclosure of COINTELPRO record required\n**(1) In general**\nNotwithstanding section 552a of title 5, United States Code, each COINTELPRO record that is not fully disclosed to the public as of the date on which the Review Board terminates under section 4(n) shall be fully disclosed to the public and made available in the Collection not later than 25 years after the date of the enactment of this Act unless\u2014\n**(A)**\nthe head of the entity of the Federal Government in the possession of control of the record, the head of a Government office, the head of the originating body, or the head of an executive agency recommends in writing the exemption of the record or particular information within the record, because the disclosure of which would clearly and demonstrably be expected to\u2014\n**(i)**\ncause identifiable or describable damage to national security, military defense, law enforcement, intelligence operations, or the conduct of foreign relations that is of such gravity that further postponing the disclosure of the record outweighs the public interest in disclosure; or\n**(ii)**\nreveal information described in paragraphs (1) through (9) of section 3.3(b) of Executive Order 13526 (75 Fed. Reg. 707; relating to classified national security information);\n**(B)**\nthe written recommendation described in subparagraph (A)\u2014\n**(i)**\nnot later than 180 days before the date that is 25 years after the date of the enactment of this Act, is provided to\u2014\n**(I)**\nthe Archivist;\n**(II)**\nthe President, if the record is in the possession or control of an agency in the executive branch of the Federal Government;\n**(III)**\nthe Chief Justice of the Supreme Court, if the record is in the possession or control of an agency in the judicial branch of the Federal Government;\n**(IV)**\nthe Speaker of the House of Representatives, if the record is in the possession or control of an office of the House of Representatives;\n**(V)**\nthe President Pro Tempore of the Senate, if the record is in the possession or control of an office of the Senate; and\n**(VI)**\nthe Speaker of the House of Representatives and the President Pro Tempore of the Senate, if the record is in the possession or control of an office of the legislative branch of the Federal Government not described under subclauses (IV) and (V); and\n**(ii)**\nincludes\u2014\n**(I)**\na justification of the recommendation to exempt the record, or particular information within the record; and\n**(II)**\na recommended date on which, or a specified occurrence following which, the record, or particular information within the record may be appropriately disclosed to the public under this Act; and\n**(C)**\nthe Archivist agrees with the written recommendation described in subparagraph (A).\n**(2) Notification**\nIf the Archivist does not agree with the recommendation described in subparagraph (A), the Archivist shall notify the person making the recommendation not later than 90 days before the date that is 25 years after the date of enactment of this Act.\n**(3) Override of decision by Archivist**\n**(A) Authority to override decision by Archivist**\nThe following individuals may override a decision of the Archivist regarding a written recommendation under paragraph (1):\n**(i)**\nThe President, if the record is in the possession or control of an agency in the executive branch of the Federal Government.\n**(ii)**\nThe Chief Justice of the Supreme Court, if the record is in the possession or control of an agency in the judicial branch of the Federal Government.\n**(iii)**\nThe Speaker of the House of Representatives, if the record is in the possession or control of an office of the House of Representatives.\n**(iv)**\nThe President Pro Tempore of the Senate, if the record is in the possession or control of an office of the Senate.\n**(v)**\nThe Speaker of the House of Representatives and the President Pro Tempore of the Senate acting jointly, if the record is in the possession or control of an agency in the legislative branch of the Federal Government.\n**(B) Notice**\nIf an individual overrides a decision described under subparagraph (A), the individual shall notify the person making the recommendation not later than 90 days before the date that is 25 years after the date of enactment of this Act.\n##### (f) Notice regarding public disclosure\n**(1) Finding**\nCongress finds that the public release of case-related documents and information without notice may significantly affect the victims of the events to which the case relates and their next of kin.\n**(2) Notice**\nNot later than 7 days before a COINTELPRO record is publicly disclosed, the entity of the Federal Government that has possession or control of the COINTELPRO record shall take all reasonable efforts to provide the COINTELPRO record to the victims of the events to which the COINTELPRO record relates, or their next of kin.\n##### (g) Definition\nIn this section, the term cause harm means to\u2014\n**(1)**\ncause identifiable or describable damage to national security, military defense, law enforcement, intelligence operations, or the conduct of foreign relations that is of such gravity that it outweighs the public interest in disclosure;\n**(2)**\nreveal information described in paragraphs (1) through (9) of section 3.3(b) of Executive Order 13526 (75 Fed. Reg. 707; relating to classified national security information);\n**(3)**\n**(A)**\nreveal the name or identity of a living individual who provided confidential information to the United States; and\n**(B)**\npose a substantial risk of harm to that individual;\n**(4)**\nconstitute an unwarranted invasion of personal privacy;\n**(5)**\n**(A)**\ncompromise the existence of an understanding of confidentiality currently requiring protection between a Government agent and a cooperating individual or group; and\n**(B)**\nbe so harmful that the understanding of confidentiality outweighs the public interest;\n**(6)**\nendanger the life or physical safety of any individual;\n**(7)**\ninterfere with ongoing law enforcement proceedings; or\n**(8)**\nreveal information as prohibited by laws and policies protecting criminal records of juveniles.\n#### 3. COINTELPRO Records Collection at the National Archives\n##### (a) In general\n**(1) Establishment of the COINTELPRO records collection**\nNot later than 60 days after the date of the enactment of this Act, the Archivist shall\u2014\n**(A)**\ncommence establishing a collection of COINTELPRO records to be known as the COINTELPRO Records Collection that ensures the physical integrity and original provenance of all records in the Collection;\n**(B)**\ncommence preparing and publishing a subject guidebook and index to the Collection; and\n**(C)**\nestablish criteria for Government offices to follow when transmitting copies of COINTELPRO records to the Archivist (to include required metadata) under subsection (d).\n**(2) Contents of Collection**\nThe Collection shall include\u2014\n**(A)**\na copy of each COINTELPRO record transmitted to the Archivist under subsection (d);\n**(B)**\nany COINTELPRO record fully disclosed to the public before the date of the enactment of the Act; and\n**(C)**\nall Review Board records, as required under this Act transmitted under section 4(l)(3).\n##### (b) Disclosure of records\nAll COINTELPRO records transmitted to the Archivist\u2014\n**(1)**\nnot later than 60 days after the transmission of the record to the Archivist, shall be available to the public for inspection and copying at the National Archives; and\n**(2)**\nshall be prioritized for digitization by the National Archives.\n##### (c) Fees for copying\nThe Archivist shall\u2014\n**(1)**\nuse efficient electronic means when possible;\n**(2)**\ncharge fees for copying COINTELPRO records in the Collection; and\n**(3)**\npromulgate regulations in accordance with the standard established under section 552(a)(4) of title 5, United States Code, for establishing procedures and guidelines for determining when such fees should be waived.\n##### (d) Transmission to the National Archives\nEach Government office shall, in accordance with the criteria established by the Archivist under subsection (a)(1)(C) as soon as is reasonably practicable, and in any event not later than 2 years after the date of the enactment of this Act, transmit to the Archivist in an electronic and searchable form a copy of each COINTELPRO record that can be partially or fully disclosed to the public in accordance with subsection (b), including any such record that is publicly available on the date of the enactment of this Act.\n#### 4. Establishment and powers of the COINTELPRO Records Review Board\n##### (a) Establishment\nThere is established, as an independent agency in the executive branch of the Federal Government, a board to be known as the COINTELPRO Records Review Board.\n##### (b) Duties of the review board\n**(1) In general**\nThe Review Board shall\u2014\n**(A)**\nreview a determination by a Government Office to partially disclose a COINTELPRO record in accordance with section 2(c); and\n**(B)**\nif such record is in the possession or control of an entity in the executive branch of the Government, make a recommendation to the President on whether the record\u2014\n**(i)**\nshould have been partially disclosed in accordance with section 2(c); or\n**(ii)**\nfully disclosed in accordance with section 2(a).\n**(2) Decisions**\nIn carrying out paragraph (1), the Review Board shall consider whether a record constitutes a COINTELPRO record.\n##### (c) Appointment\n**(1) In general**\nThe President shall appoint, by and with the advice and consent of the Senate, 5 individuals to serve as members of the Review Board.\n**(2) Initial appointment**\n**(A) In general**\nSubject to subparagraph (C), initial appointments to the Review Board shall be made not later than 60 days after the date of the enactment of this Act.\n**(B) Recommendations**\nIn making appointments to the Review Board, the President may consider any individuals recommended by the American Historical Association, the Organization of American Historians, the Society of American Archivists, and the American Bar Association.\n**(C) Extension**\nIf an organization described in subparagraph (B) does not recommend at least 2 nominees meeting the qualifications stated in paragraph (3) within 60 days after the date of the enactment of this Act, the deadline under subparagraph (A) shall be extended until the earlier of 60 days after the date on which such recommendations are made or 120 days after the date of the enactment of this Act.\n**(D) Additional recommendations**\nThe President may request that any organization described in subparagraph (B) submit additional recommended nominees.\n**(3) Qualifications**\nIndividuals nominated to the Review Board shall\u2014\n**(A)**\nnot have had any previous involvement with any official investigation or inquiry conducted by the Federal Government, or any State or local government, relating to any COINTELPRO;\n**(B)**\nbe distinguished individuals of high national professional reputation in their respective fields who are capable of exercising the independent and objective judgment necessary to fulfill their role in ensuring and facilitating the review, transmission to the public, and public disclosure of files related to COINTELPRO and who possess an appreciation of the value of such material to the public, scholars, and government; and\n**(C)**\ninclude at least 1 professional historian and 1 attorney.\n##### (d) Security clearances\nAll Review Board nominees may be processed for the necessary security clearances in an accelerated manner by the appropriate Federal agencies and subject to the standard procedures for granting such clearances.\n##### (e) Vacancy\nA vacancy on the Review Board shall be filled in the same manner as the original appointment and within 60 days of the occurrence of the vacancy.\n##### (f) Chairperson\nThe members of the Review Board shall elect 1 of the members as chairperson.\n##### (g) Removal of Review Board member\n**(1) In general**\nNo member of the Review Board shall be removed from office, other than\u2014\n**(A)**\nby impeachment and conviction; or\n**(B)**\nby the action of the President for inefficiency, neglect of duty, malfeasance in office, physical disability, mental incapacity, or any other condition that substantially impairs the performance of the member\u2019s duties.\n**(2) Report**\n**(A) In general**\nIf a member of the Review Board is removed from office, and that removal is by the President, not later than 10 days after the removal, the President shall submit to the Committee on Oversight and Accountability of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report specifying the facts found and the grounds for the removal.\n**(B) Publication**\nThe President shall publish in the Federal Register a report submitted under subparagraph (A), except that the President may, if necessary to protect the rights of a person named in the report or to prevent undue interference with any pending prosecution, postpone or refrain from publishing any or all of the report until the completion of such pending cases or pursuant to privacy protection requirements in law.\n**(3) Judicial review**\n**(A) In general**\nA member of the Review Board removed from office may obtain judicial review of the removal in a civil action commenced in the United States District Court for the District of Columbia.\n**(B) Relief**\nThe member may be reinstated or granted other appropriate relief by order of the court.\n##### (h) Compensation of members\n**(1) In general**\nA member of the Review Board shall be compensated at a rate equal to the daily equivalent of the annual rate of basic pay prescribed for level IV of the Executive Schedule under section 5315 of title 5, United States Code, for each day (including travel time) during which the member is engaged in the performance of the duties of the Review Board.\n**(2) Travel expenses**\nA member of the Review Board shall be allowed reasonable travel expenses, including per diem in lieu of subsistence, at rates for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from the member\u2019s home or regular place of business in the performance of services for the Review Board.\n##### (i) Powers\n**(1) In general**\nThe Review Board shall have the authority to act in a manner prescribed under this Act including the authority to\u2014\n**(A)**\ndirect a Government office to make available to the Review Board, and if necessary investigate the facts surrounding, additional information, records, or testimony from individuals, which the Review Board has reason to believe is required to fulfill its functions and responsibilities under this Act;\n**(B)**\nsubpoena private persons to compel the production of documents and other records relevant to its responsibilities under this Act;\n**(C)**\nrequire any Government office to account in writing for the destruction of any records relating to COINTELPRO;\n**(D)**\nreceive information from the public regarding the identification and public disclosure of COINTELPRO records; and\n**(E)**\nhold hearings and administer oaths.\n**(2) Enforcement of subpoenas**\nThe Review Board may bring a civil action in a district court of the United States to enforce a subpoena issued under paragraph (1)(B).\n##### (j) Witness immunity\nThe Review Board shall be considered to be an agency of the United States for purposes of chapter 601 of title 18, United States Code.\n##### (k) Support services\nThe Administrator of General Services shall provide administrative services for the Review Board on a reimbursable basis.\n##### (l) Termination\n**(1) In general**\nThe Review Board shall terminate not later than 4 years after the date of enactment of this Act, except that the Review Board may, by majority vote, extend its term for an additional 1-year period if the Review Board determines that it has not completed its work within that 4-year period.\n**(2) Reports**\nBefore its termination, the Review Board shall\u2014\n**(A)**\nsubmit a report to the President and the Congress on the activities conducted by the Board, including a complete and accurate accounting of expenditures during its existence; and\n**(B)**\ncomplete all other reporting requirements under this Act.\n**(3) Transfer of records**\n**(A) In general**\nUpon termination, the Review Board shall transfer all records created by or in the possession of the Board to the Archivist for inclusion in the Collection.\n**(B) Preservation of records**\nThe records of the Review Board shall not be destroyed, except that the Archivist may destroy routine administrative records covered by a general records schedule following notification in the Federal Register and after considering comments.\n#### 5. COINTELPRO Records Review Board personnel\n##### (a) Chief of staff\n**(1) Appointment**\nNot later than 45 days after the initial meeting of the Review Board, and without regard to political affiliation, the Review Board shall appoint an individual to the position of Chief of Staff of the Review Board.\n**(2) Requirements**\nThe individual appointed as Chief of Staff\u2014\n**(A)**\nshall be a citizen of the United States of integrity and impartiality who is a distinguished professional; and\n**(B)**\nshall have had no previous involvement with any official investigation or inquiry relating to COINTELPRO.\n**(3) Candidate to have clearances**\nA candidate for Chief of Staff may be granted the necessary security clearances in an accelerated manner subject to the standard procedures for granting such clearances.\n**(4) Approval contingent on prior clearance**\nA candidate for Chief of Staff may not be appointed without receiving a security clearance.\n**(5) Duties**\nThe Chief of Staff shall\u2014\n**(A)**\nserve as principal liaison to Government offices;\n**(B)**\nbe responsible for the administration and coordination of the Review Board\u2019s review of records;\n**(C)**\nbe responsible for the administration of all official activities conducted by the Review Board; and\n**(D)**\nhave no authority to decide or determine whether any record shall be disclosed to the public or postponed for disclosure.\n**(6) Removal**\nThe Chief of Staff shall not be removed except upon a majority vote of the Review Board to remove the Chief of Staff for cause on the grounds of inefficiency, neglect of duty, malfeasance in office, physical disability, mental incapacity, or any other condition that substantially impairs the performance of the responsibilities of the Chief of Staff or the employees of the Review Board.\n##### (b) Staff\n**(1) Additional personnel**\nThe Review Board may appoint additional employees as are necessary to enable the Review Board and its Chief of Staff to perform their duties. Any employee appointed under this paragraph shall be in the excepted service (as that term is defined in section 2103 of title 5, United States Code).\n**(2) Requirements**\nAn individual appointed as an employee of the Review Board\u2014\n**(A)**\nshall be a private citizen of integrity and impartiality; and\n**(B)**\nshall have had no previous involvement with any official investigation or inquiry relating to COINTELPRO.\n**(3) Nominations**\nBefore making an appointment pursuant to paragraph (1), the Review Board shall consider individuals recommended by the American Historical Association, the Organization of American Historians, the Society of American Archivists, and the American Bar Association.\n**(4) Security clearances**\nA staff candidate may not be appointed without receiving a security clearance.\n##### (c) Compensation\nThe Review Board shall fix the compensation of the Chief of Staff and other employees in accordance with title 5, United States Code, except that the rate of pay for the Chief of Staff and other employees may not exceed the rate payable for level V of the Executive Schedule under section 5316 of that title.\n##### (d) Advisory committees\nThe Review Board may create advisory committees to assist in fulfilling the responsibilities of the Review Board under this Act.\n#### 6. Review of records by the COINTELPRO Records Review Board\n##### (a) Custody of records reviewed by the review board\nPending a determination by the Review Board with respect to a record transmitted to the Board for review under this section, a Government office shall retain custody of a COINTELPRO record for purposes of preservation, security, and efficiency, unless\u2014\n**(1)**\nthe Review Board requires the physical transfer of records for reasons of conducting an independent and impartial review; or\n**(2)**\nsuch transfer is necessary for an administrative hearing or other official Review Board function.\n##### (b) Recommendation of the Review Board\n**(1) In general**\nIn reviewing a record in accordance with section 4(b), the Review Board shall direct that copies of all COINTELPRO records be transmitted to the Archivist and fully disclosed to the public in the Collection in the absence of clear and convincing evidence that\u2014\n**(A)**\na record is not a COINTELPRO record; or\n**(B)**\na record or particular information within a COINTELPRO record does not cause harm, as such term is defined in section 2.\n**(2) Postponement**\nIn determining whether a COINTELPRO record should be fully disclosed to the public under section 2(a), the Review Board shall work to\u2014\n**(A)**\nprovide for the disclosure of segregable parts, substitutes, or summaries of such a record; and\n**(B)**\ndetermine, in consultation with the Government office in the possession or control of the record, and consistent with the standards for disclosure under this Act, which of the following alternative forms of disclosure shall be made by the Government office:\n**(i)**\nAny reasonably segregable particular information in a COINTELPRO record.\n**(ii)**\nA substitute record for that information which is postponed.\n**(3) Report**\nWith respect to a COINTELPRO record, or particular information within a record, for which only substitutions or summaries have been disclosed to the public, the Review Board shall transmit to the Archivist a report containing\u2014\n**(A)**\na description of actions by the Review Board, the originating body, the President, or any Government office (including a justification of any such action to postpone disclosure of any record or part of any record) and of any official proceedings conducted by the Review Board with regard to specific COINTELPRO records; and\n**(B)**\na statement, based on a review of the proceedings and in conformity with the decisions reflected therein, designating a recommended specified time at which or a specified occurrence following which the material may be appropriately disclosed to the public under this Act.\n**(4) Notice**\nNot later than 14 days after the Review Board makes a determination whether a COINTELPRO record should be fully disclosed, the Review Board shall\u2014\n**(A)**\nnotify the head of the Government office in the possession or control of the record of the determination; and\n**(B)**\npublish a copy of the determination in the Federal Register.\n##### (c) Notice to the public\nOn each day that is on or after the date that is 60 days after the Review Board first approves the postponement of disclosure of a COINTELPRO record, the Review Board shall publish on a publicly available website a notice that summarizes the recommendation including a description of the subject, the originating body, length or other physical description, and each justification relied on for the recommendation.\n##### (d) Reports by the Review Board\n**(1) In general**\nThe Review Board shall submit a report its activities to the Speaker of the House of Representatives, the Minority Leader of the House of Representatives, the Committee on Oversight and Accountability of the House of Representatives, the Majority Leader of the Senate, the Minority Leader of the Senate, the Committee on Homeland Security and Governmental Affairs of the Senate, the President, the Archivist, and the head of any Government office whose records have been the subject of Review Board activity.\n**(2) Deadlines**\nNot later than 1 year after the date of the enactment of this Act, and every year thereafter until the termination of the Review Board, the Review Board shall issue a report under paragraph (1).\n**(3) Contents**\nEach report under paragraph (1) shall include the following information:\n**(A)**\nA financial report of the expenses for all official activities and requirements of the Review Board and its employees.\n**(B)**\nThe progress made on review and, transmission to the Archivist, and public disclosure of COINTELPRO records.\n**(C)**\nThe estimated time and volume of COINTELPRO records involved in the completion of the Review Board\u2019s duties under this Act.\n**(D)**\nAny special problems, including requests and the level of cooperation of Government offices, with regard to the ability of the Review Board to meet the requirements of this Act.\n**(E)**\nA record of review activities, including a record of recommendations that a record not be fully disclosed by the Review Board or other related actions authorized by this Act, and a record of the volume of records reviewed and recommended to not be fully disclosed.\n**(F)**\nRecommendations and requests to Congress for additional authorizations or appropriations.\n**(G)**\nAn appendix containing copies of reports of postponed records to the Archivist required under subsection (c)(3) made since the date of the preceding report submitted under this subsection.\n**(4) Notice of termination**\nNot later than 90 days before terminating, the Review Board shall provide written notice to the President and the Congress of its intention to terminate its operations at a specified date and the date on which the Board intends to terminate.\n#### 7. Disclosure of other information and additional study\n##### (a) Materials under the seal of the court\n**(1) In general**\nThe Review Board may request the Attorney General to petition any court in the United States to release any information relevant to COINTELPRO that is held under seal of court.\n**(2) Grand jury materials**\n**(A) In general**\nThe Review Board may request the Attorney General to petition any court in the United States to release any information relevant to COINTELPRO that is held under the injunction of secrecy of a grand jury.\n**(B) Particularized need**\nA request for disclosure of COINTELPRO records under this Act shall be deemed to constitute a showing of particularized need pursuant to rule 6 of the Federal Rules of Criminal Procedure.\n**(3) Deadline**\n**(A) In general**\nThe Attorney General shall respond to any request that is subject to this subsection within 45 days.\n**(B) Nondisclosure of grand jury information**\nIf the Attorney General determines that information relevant to a COINTELPRO that is held under the seal of a grand jury should not be made public, the Attorney General shall set forth in the response to the request the reasons for the determination.\n##### (b) Cooperation with agencies\nIt is the sense of Congress that\u2014\n**(1)**\nthe Attorney General should assist the Review Board in good faith to unseal any records that the Review Board determines to be relevant and held under the seal by a court or under the injunction of secrecy of a grand jury; and\n**(2)**\nall Government offices should cooperate in full with the Review Board to seek the disclosure of all information relevant to COINTELPRO consistent with the public interest.\n#### 8. Rules of construction\n##### (a) Precedence over other law\n**(1) In general**\nSubject to paragraph (2), when this Act requires transmission of a record to the Archivist or public disclosure, it shall take precedence over any other law (except section 6103 of the Internal Revenue Code of 1986 ( 26 U.S.C. 6103 )), judicial decisions construing such law, or common law doctrine that would otherwise prohibit such transmission or disclosure with the exception of deeds governing access to or transfer or release of gifts and donations of records to the United States Government.\n**(2) Personnel and medical files**\nThis Act shall not require the public disclosure of personnel and medical files and similar files the disclosure of which would constitute a clearly unwarranted invasion of personal privacy.\n##### (b) Freedom of Information Act\nNothing in this Act shall be construed to eliminate or limit any right to file any requests with any executive agency or seek judicial review of a decision under section 552 of title 5, United States Code.\n##### (c) Judicial review\nNothing in this Act shall be construed to preclude judicial review, under chapter 7 of title 5, United States Code, of final actions taken or required to be taken under this Act.\n##### (d) Existing authority\nNothing in this Act revokes or limits the existing authority of the President, any executive agency, the Senate, the House of Representatives, or any other entity of the Government to publicly disclose records in its possession.\n#### 9. Redesignation\nThe Federal building located at 935 Pennsylvania Avenue Northwest in Washington, DC, commonly known as the J. Edgar Hoover Federal Building, shall be known and designated as the Federal Bureau of Investigation Federal Building .\n#### 10. References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the Federal building referred to in section 3 shall be deemed to be a reference to the Federal Bureau of Investigation Federal Building .\n#### 11. Funding\nUntil such time as funds are appropriated to carry out this Act, the President shall use such sums as are available for discretionary use to carry out this Act.\n#### 12. Definitions\nIn this Act:\n**(1) Archivist**\nThe term Archivist means the Archivist of the United States.\n**(2) COINTELPRO**\nThe term COINTELPRO means the covert and illegal counter intelligence program conducted by the Federal Bureau of Investigation in 1956 that involved surveilling, infiltrating, discrediting, and disrupting domestic organizations involved in the political process, including political parties, non-governmental organizations, advocacy groups, and special interest groups.\n**(3) COINTELPRO record**\nThe term COINTELPRO record means a record that\u2014\n**(A)**\nis related to COINTELPRO; and\n**(B)**\nwas created or made available for use by, obtained by, or otherwise came into the possession of\u2014\n**(i)**\nan entity of the Federal Government, including\u2014\n**(I)**\nthe Library of Congress;\n**(II)**\nany executive agency, including the National Archives; and\n**(III)**\nany independent agency; or\n**(ii)**\nany State or local government, or component thereof, that provided support or assistance or performed work in connection with a Federal inquiry into surveillance, infiltration, discrediting, or disruption undertaken as a part of COINTELPRO.\n**(4) Collection**\nThe term Collection means the COINTELPRO Records Collection established under section 3.\n**(5) Executive agency**\nThe term executive agency means an agency, as defined in section 552(f) of title 5, United States Code.\n**(6) Government office**\nThe term Government office means any entity of the Federal Government that has possession or control of 1 or more COINTELPRO record.\n**(7) Government official**\nThe term Government official means any officer or employee of the United States, including any elected or appointed official.\n**(8) National Archives**\nThe term National Archives means the National Archives and Records Administration and all components thereof, including Presidential archival depositories established under section 2112 of title 44, United States Code.\n**(9) Official investigation**\nThe term official investigation means the review of a COINTELPRO case conducted by any entity of the Federal Government either independently, at the request of any Presidential commission or congressional committee, or at the request of any Government official.\n**(10) Originating body**\nThe term originating body means the entity of the Federal Government, or the entity of a State or local government, as the case may be, that created a record or particular information within a record.\n**(11) Public interest**\nThe term public interest means the compelling interest in the prompt public disclosure of civil rights cold case records for historical and Governmental purposes and for the purpose of fully informing the people of the United States about the history surrounding all civil rights cold cases in the United States.\n**(12) Record**\nThe term record has the meaning given the term in section 3301 of title 44, United States Code.\n**(13) Review Board**\nThe term Review Board means the COINTELPRO Records Review Board established under section 4.",
      "versionDate": "2026-01-22",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-18T16:03:37Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7220ih.xml"
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
      "title": "COINTELPRO Full Disclosure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COINTELPRO Full Disclosure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the public disclosure of COINTELPRO records, to establish a COINTELPRO Records Collection, and to establish the COINTELPRO Records Review Board, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:33:40Z"
    }
  ]
}
```
