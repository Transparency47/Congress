# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3127?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3127
- Title: Fairness to Freedom Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3127
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-03-28T08:06:26Z
- Update date including text: 2026-03-28T08:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3127",
    "number": "3127",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Fairness to Freedom Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-28T08:06:26Z",
    "updateDateIncludingText": "2026-03-28T08:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "WA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MI"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "DC"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "IL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "OR"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3127ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3127\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mrs. Torres of California (for herself, Ms. Meng , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish the right to counsel, at Government expense for those who cannot afford counsel, for people facing removal.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Fairness to Freedom Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTitle I\u2014Guaranteeing the right to counsel\nSec. 101. Guaranteeing and expanding the right to counsel.\nSec. 102. Public charge.\nTitle II\u2014Office of Immigration Representation\nSec. 201. Definitions.\nSec. 202. Establishment; purpose; independence.\nSec. 203. Board of Directors.\nSec. 204. Director.\nSec. 205. Employees.\nSec. 206. Local immigration representation boards.\nSec. 207. Types of immigration defenders.\nSec. 208. Compensation and reimbursement of expenses of counsel.\nSec. 209. Services other than counsel.\nSec. 210. Immigration Representation Advisory Board.\nTitle III\u2014Authorization of appropriations\nSec. 301. Authorization of appropriations.\nSec. 302. Minimum funding for the Office of Immigration Representation.\nI\nGuaranteeing the right to counsel\n#### 101. Guaranteeing and expanding the right to counsel\nSection 292 of the Immigration and Nationality Act ( 8 U.S.C. 1362 ) is amended to read as follows:\n292. Right to counsel (a) In general Any individual in any removal, exclusion, deportation, bond, or expedited removal proceeding under section 212(d)(5)(A), 235(b)(1)(B), 236, 238, 240, or 241 or in any matter related to any such proceeding before U.S. Citizenship and Immigration Services, any State court, or any court created under article III of the Constitution of the United States, any individual who is financially unable to obtain representation subject to such proceeding shall be entitled to legal representation at Government expense in accordance with this section. (b) Matters included Proceedings and matters referred to in subsection (a) shall include\u2014 (1) petitions for a writ of habeas corpus under section 2241 of title 28, United States Code, or any other similar proceeding; (2) administrative and judicial proceedings for individuals who may be eligible for special immigrant juvenile status under section 1101(a)(27)(J)(ii) of title 8, United States Code; (3) applications before the U.S. Citizenship and Immigration Services related to relief from removal, and post-conviction relief in criminal proceedings; (4) post-conviction relief in criminal proceedings; and (5) any other legal proceeding involving an individual described in subsection (a) that is related to such individual's legal status in the United States. (c) Scope of counsel (1) Advocacy Consistent with Rule 1.3 of the American Bar Association's Model Rules of Professional conduct, attorneys and other persons providing representation to individuals in proceedings or matters described in subsection (a) shall\u2014 (A) act with reasonable diligence, promptness, commitment, and dedication to the interests of the client and with zeal in advocating on the client\u2019s behalf; and (B) hold the Government to its burden by presenting the fullest defense possible in each such proceeding or matter. (2) Scope of representation Representation under this section shall include\u2014 (A) counsel and interpretation and translation services; and (B) any other services that are necessary for effective representation, including the services described in section 309 of the Fairness to Freedom Act of 2025 . (3) Commencement of representation (A) In general The right to counsel of a person detained in, or released from, the custody of the Department of Homeland Security or the Department of Health and Human Services shall attach at the earlier of\u2014 (i) the placement of the person in the custody of either department, regardless of whether the person has been formally placed in a proceeding described in subsection (a); or (ii) the issuance to the person of a Notice to Appear or other document initiating proceedings under section 235, 238, 240, or 241. (B) Clarification The appointment of counsel based on the issuance of a Notice to Appear shall occur regardless of whether the Notice to Appear has been filed with the immigration court. The appointment of counsel for a detained person shall occur as soon as possible, but in no event later than 24 hours after such person is taken into the custody of the Department of Homeland Security. (4) Continuous representation (A) In general An individual for whom counsel is appointed under this section shall be represented continuously at every stage of proceedings beginning with the initial appearance before any official with adjudicatory authority and including any proceedings before the Immigration Courts, the Board of Immigration Appeals, Federal district courts, Federal courts of appeal, and the United States Supreme Court, including ancillary matters related to the proceedings described in subsection (a), and ending when all such proceedings have concluded. (B) Appointment of different counsel If the nature of the representation needed by a person in proceedings under this section requires the appointment of different representatives for different stages of such proceedings, all such representatives shall comply with the minimum standards of representation described in paragraph (1). (C) Appointment of new counsel after relocation The Office of Immigration Representation established under section 202 of the Fairness to Freedom Act of 2025 shall ensure that each individual who is released from custody and moves to a State or municipality other than the State or municipality in which he or she was in custody, or who is transferred to a detention facility in another State or municipality is provided with counsel in the new State or municipality in which the individual resides or is detained. (5) Construction This subsection shall be broadly construed to attach in any proceeding and related matter, including any petition for review or appellate process, request for re-interview, request for reconsideration, and motion to reopen, arising from a proceeding or matter described in subsection (a). (d) Eligibility and commencement of immigration proceedings (1) Notification A proceeding described in subsection (a) shall not commence until counsel has been appointed to represent the individual subject to such proceeding. If such a proceeding has already commenced without the appointment of counsel, such proceeding shall be paused until such counsel is appointed. Before commencing a proceeding described in subsection (a), the adjudicatory official, who may be an official of U.S. Immigration and Customs Enforcement or of U.S. Customs and Border Protection, under a plan approved by the Office of Immigration Representation, shall notify the individual subject to such proceeding that\u2014 (A) such individual has the right to be represented by counsel; and (B) counsel will be appointed to represent such individual before the commencement of such proceeding if the individual\u2014 (i) has not retained private counsel; and (ii) is financially unable to obtain counsel. (2) Determination of financial ability to obtain counsel (A) In general An individual shall be deemed to be financially unable to obtain counsel under paragraph (1)(B)(ii) if the individual\u2019s net financial resources and income are insufficient to obtain qualified counsel. (B) Eligibility for counsel An individual who makes a sworn statement to the adjudicatory official referred to in subsection (a) that he or she is a member of a family whose income is not more than 200 percent of the poverty line (as defined in section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) )) is eligible for Government-appointed counsel under this section. (3) Access to pertinent documents and information (A) In general An individual described in subsection (a) and his or her counsel shall automatically receive a complete copy of all documents and information pertaining to such individual that are in the possession of the Department of Homeland Security or the Department of Health and Human Services, including documents obtained from other Government agencies, unless the disclosure of any such document or information is barred by privilege or otherwise prohibited by law. (B) Records Not later than 7 days after counsel is appointed to represent an individual under this Act, the Director of U.S. Citizenship and Immigration Services shall\u2014 (i) provide such individual and counsel with a complete copy of the individual\u2019s immigration file (commonly known as the A-file ); and (ii) facilitate the provision to such individual and counsel of a copy of any Record of Proceeding that is in the possession of the Department of Homeland Security, the Department of Health and Human Services, or the Department of Justice (other than documents protected from disclosure under section 552(b) of title 5, United States Code). (4) Restriction A proceeding described in subsection (a) may not commence before the date that is 10 days after the date on which the individual, or the individual's counsel, has received all of the documents described in paragraph (3), in order to review and assess such documents, unless the individual or his or her counsel knowingly and voluntarily waives such restriction. (e) Appointment of counsel (1) Notification requirement If an individual who is entitled to representation under this section is not represented by counsel, the adjudicatory official shall\u2014 (A) notify the Local Administrator appointed pursuant to section 206(k)(3) of the Fairness to Freedom Act of 2025 (or the designee of the Local Administrator) that such individual is not represented by counsel; and (B) advise such individual\u2014 (i) of his or her right to be represented by counsel; and (ii) that such counsel will be appointed if such person is financially unable to obtain counsel. (2) Waiver An individual's right to be represented by appointed counsel may only be waived by the individual\u2014 (A) in the physical presence of appointed counsel; (B) if such waiver is knowing and voluntary; and (C) if the individual demonstrates that he or she\u2014 (i) understands the nature of any charges and the possible defenses and outcomes; and (ii) possesses the knowledge and intelligence necessary to conduct his or her own defense. (3) Appeal of waiver; retroactive appointment Counsel may appeal any putative waiver to the Office of Immigration Representation established under section 202 of the Fairness to Freedom Act of 2025 if counsel reasonably believes that such waiver did not meet the requirements under paragraph (2). If the Office of Immigration Representation concurs with counsel's assessment, the Office may retroactively appoint counsel in order to include any representation furnished pursuant to the plan before such appointment. (4) Appointment of counsel Unless an individual waives representation by counsel pursuant to paragraph (2), the Local Administrator, upon notification that an individual may meet the criteria for appointed counsel, shall appoint counsel for such individual in accordance with the Local Plan developed pursuant to section 206(k)(1) of the Fairness to Freedom Act of 2025 if the Local Administrator determines, after appropriate inquiry, that such individual is financially unable to obtain counsel. An appointment under this paragraph may be made retroactive to include any representation furnished to such individual by such counsel before such appointment. (5) Appointment of separate counsel The Local Administrator shall appoint separate counsel for individuals who are subjected to the same proceeding or related proceedings if\u2014 (A) the interests of such individuals cannot, consistent with ethical responsibilities and manageable workloads, be properly be represented by a single counsel; or (B) the Local Administrator demonstrates another good cause for appointing separate counsel. (6) Consolidated cases (A) In general Subject to paragraph (5) and except as provided in subparagraph (B), if the Attorney General consolidates the case of an individual for whom counsel was appointed pursuant to subsection (a) with the case of another individual without counsel, the counsel appointed pursuant to subsection (a) shall be appointed to represent such other individual unless a conflict of interest would prevent joint representation. (B) Conflict of interest If a conflict of interest prevents joint representation under subparagraph (A), the Local Administrator shall appoint separate counsel for the individuals referred to in such subparagraph unless the Local Administrator demonstrates that there is a good cause for not appointing separate counsel. (7) Change of financial circumstances during proceedings If an individual who has retained counsel becomes financially unable to pay such counsel and is eligible for appointed counsel under this section, the Local Administrator may appoint counsel for such individual in accordance with this section. (8) Substitution of counsel The Local Administrator, in the interests of justice, upon a showing of good cause, and consistent with ethical requirements applicable to attorneys practicing in the region, substitute an appointed counsel for another appointed counsel at any stage of a proceeding referred to in subsection (a). (f) Access to counsel (1) In general If an individual is subject to proceedings described in subsection (a) or to detention or inspection at a port of entry, U.S. Customs and Border Protection, U.S. Immigration and Customs Enforcement, or the Office of Refugee Resettlement, as appropriate, shall\u2014 (A) facilitate access for such individual to counsel; and (B) ensure that counsel appointed under this section is permitted to meet in person with such individual in a confidential, private setting when requested during the first 12 hours the individual is detained and as soon as practicable after subsequent meeting requests. (2) Alternative meeting options If counsel appointed pursuant to this section cannot personally meet with an individual described in paragraph (1) to whom such counsel was appointed to represent, U.S. Customs and Border Protection, U.S. Immigration and Customs Enforcement, or the Office of Refugee Resettlement, as appropriate, at the request of such individual or the counsel of the individual, shall provide alternative options through which counsel may communicate with such individual remotely in a confidential, private manner during the first 12 hours such individual is detained and as soon as practicable after subsequent meeting requests. (3) Effect of failure to provide timely access to counsel If U.S. Customs and Border Protection, U.S. Immigration and Customs Enforcement, or the Office of Refugee Resettlement, as applicable, fails to timely provide an individual with access to counsel in accordance with paragraph (1) or (2), no statement made by the individual before such access has been made available may be introduced into evidence against the respondent except on a motion by the appointed counsel, who shall be entitled to a continuance in the proceedings giving rise to the appointment of such counsel. (4) Limitation An individual held or detained at a port of entry may not submit a valid Record of Abandonment of Lawful Permanent Resident Status or Withdrawal of Application for Admission if U.S. Customs and Border Protection or U.S. Immigration and Customs Enforcement has failed to provide such individual with access to counsel in accordance with this section. (5) Institutional hearing program Individuals held in Federal, State, or local criminal custody who are placed in any proceeding described in subsection (a) shall be ensured access to counsel consistent with the requirements of this section. No statement made by the respondent before such access has been made available may be introduced into evidence against the respondent except on appointed counsel\u2019s own motion. Counsel shall be entitled to a continuance in the proceedings giving rise to his or her appointment. (6) Termination of proceedings If the Local Administrator fails to provide counsel to an individual in accordance with this section, the Secretary of Homeland Security or the Attorney General, as appropriate, shall terminate any proceedings involving such individual with prejudice. .\n#### 102. Public charge\nSeeking or receiving appointed counsel under section 292 of the Immigration and Nationality Act, as amended by section 101, may not be serve as the basis for any determination that the individual seeking or receiving such services is likely to become a public charge for the purposes of determining the admissibility, removability, excludability, or deportability of such individual under such Act, or in any other proceeding in which such individual\u2019s likelihood of becoming a public charge is at issue for immigration purposes.\nII\nOffice of Immigration Representation\n#### 201. Definitions\nIn this title:\n**(1) Board**\nThe term Board means the Board of Directors of the Office.\n**(2) Director**\nThe term Director means the Director of the Office of Immigration Representation appointed pursuant to section 206(k)(1).\n**(3) Immigration public defender organization**\nThe term Immigration Public Defender Organization means an organization established by a Local Board pursuant to section 207(a)(1).\n**(4) Local board**\nThe term Local Board means a local immigration representation board established within a region pursuant to section 206(a).\n**(5) Office**\nThe term Office means the Office of Immigration Representation established under section 202(a).\n#### 202. Establishment; purpose; independence\n##### (a) Establishment\nThere is established in the District of Columbia a private nonprofit corporation, which shall be known as the Office of Immigration Representation.\n##### (b) Purpose\nThe purpose of the Office shall be to ensure high-quality legal representation and related services to all individuals described in section 292(a) of the Immigration and Nationality Act, as amended by section 101, who cannot afford representation.\n##### (c) Independence\nExcept as otherwise provided in this Act, the Office shall exercise its authority independently of any Government official, agency, or department, including the Department of Justice, the Department of Homeland Security, and the Department of Health and Human Services.\n#### 203. Board of Directors\n##### (a) Number and appointment\n**(1) In general**\nThe Office shall be governed by a Board of Directors, consisting of 24 members who shall be appointed not later than 1 year after the date of the enactment of this Act, in accordance with paragraph (2).\n**(2) Initial judicial appointments**\n**(A) In general**\nSubject to subparagraphs (B) and (C), the chief judge of each United States Court of Appeals (except for the chief judge for the Federal Circuit) shall appoint 2 individuals to the Board who meet the requirements set forth in subsection (b).\n**(B) Staggered terms of service**\nThe terms of service of the members of the Board appointed pursuant to subparagraph (A) shall be staggered so that\u2014\n**(i)**\n6 members serve an initial term of 1 year;\n**(ii)**\n6 members serve an initial term of 2 years;\n**(iii)**\n6 members serve an initial term of 3 years; and\n**(iv)**\n6 members serve an initial term of 4 years.\n**(C) Circuits**\n**(i) Eastern circuits**\nThe chief judge of the 1st, 2nd, 3rd, 4th, 11th, and DC Circuit Courts of Appeals shall appoint 1 individual to serve an initial term of 1 year and 1 individual to serve an initial term of 4 years.\n**(ii) Remaining circuits**\nThe chief judge of the 5th, 6th, 7th, 8th, 9th, and 10th Circuit Courts of Appeals shall appoint 1 individual to serve an initial term of 2 years and 1 individual to serve an initial term of 3 years.\n**(3) Immigration Representation Advisory Board appointments**\n**(A) Initial appointments**\nUpon the expiration of the initial term of the 6 members of the Board who were appointed to 1-year terms pursuant to paragraph (2)(B)(i), the Immigration Representation Advisory Board established under section 210 shall appoint to 4-year terms\u2014\n**(i)**\n6 members of the Board;\n**(ii)**\nan Immigration Public Defender, who shall serve as a nonvoting, ex-officio member of the Board; and\n**(iii)**\na Panel Attorney, who shall serve as a nonvoting, ex-officio member of the Board.\n**(B) Subsequent appointments**\nUpon the expiration of the initial term of the 6 members of the Board who were appointed to 2-year terms pursuant to paragraph (2)(B)(ii), the Immigration Representation Advisory Board established under section 210 shall appoint 6 members of the Board to 4-year terms. The Immigration Representation Advisory Board shall also appoint individuals to replace any member of the Board who had been appointed by the Advisory Board, upon the expiration of such member's term.\n**(4) Subsequent judicial appointments**\n**(A) In general**\nUpon the expiration of the term of any member of the Board appointed by a chief judge to a 3-year or 4-year term, such chief judge shall appoint an individual to the Board from a list of 5 qualified individuals nominated, by majority vote, by a committee consisting of\u2014\n**(i)**\nthe head of each Immigration Public Defender Organization that is headquartered within the corresponding circuit;\n**(ii)**\nthe head of each Community Defender Office that is headquartered within the corresponding circuit; and\n**(iii)**\npanel attorney representatives within the corresponding circuit.\n**(B) Failure to produce list**\nIf a committee described in subparagraph (A) from a circuit does not provide a list of 5 Board nominees to the chief judge of the corresponding circuit before the date that is 30 days after the expiration of the term of service of a member of the Board representing such circuit, the chief judge of such circuit may appoint an individual to replace such member of the Board without regard to nominations.\n##### (b) Restrictions on membership\n**(1) Qualifications**\nEach individual appointed to the Board pursuant to subsection (a)\u2014\n**(A)**\nshall be nonpartisan;\n**(B)**\nshall have significant experience representing persons in proceedings described in section 292(a) of the Immigration and Nationality Act, as amended by section 101 of this Act; and\n**(C)**\nshall have demonstrated a strong commitment to representation in indigent defense matters.\n**(2) Diversity**\nIn making appointments to the Board under subsection (a), chief judges and the Immigration Representation Advisory Board shall seek to appoint individuals, in the aggregate, who reflect the characteristics of the population represented by counsel appointed pursuant section 292 of the Immigration and Nationality Act, including the characteristics of race, gender identity, sexual orientation, immigration experience, and socioeconomic background.\n**(3) Disqualifying characteristics**\nA member of the Board, while serving in such capacity, may not be\u2014\n**(A)**\nan employee of the Office or a member of a Local Board, an Immigration Public Defender Organization or Community Defender Office, or a Panel Attorney, unless he or she is serving as an ex-officio member of the Board;\n**(B)**\na judge or employee of any Federal or State court, any immigration court, or the Board of Immigration Appeals; or\n**(C)**\na prosecutor or law enforcement officer or employee thereof, or any person who has held such a position during the 3-year period immediately preceding his or her appointment to the Board.\n##### (c) Term of membership\n**(1) Maximum length of service**\nNo member of the Board may serve more than 2 terms, except that a person who was appointed to serve a 1-year term may be appointed to 2 additional 4-year terms.\n**(2) Replacement members**\nA person who is appointed to replace a member who resigned or was removed\u2014\n**(A)**\nshall serve the remainder of the term of such member; and\n**(B)**\nmay be appointed to serve up to 2 additional 4-year terms.\n##### (d) Vacancies\n**(1) Members selected by a chief judge**\nNot later than 90 days after the creation of a vacancy arising from a Board member position selected by a chief judge, the committee described in subsection (a)(2)(A) from the corresponding circuit shall submit a list of 5 qualified nominees to such chief judge, who shall appoint 1 of such nominees as the new member of the Board.\n**(2) Failure to produce list**\nIf the committee fails to submit the list required under paragraph (1) before the deadline, the chief judge may make a selection without regard to nominations.\n**(3) Members selected by the immigration representation advisory board**\nNot later than 90 days after the creation of a vacancy arising from a Board member position selected by the Immigration Representation Advisory Board, the Immigration Representation Advisory Board shall appoint a new member of the Board to fill such vacancy.\n##### (e) Rates of pay; travel expenses\n**(1) Rates of pay**\nMembers shall be paid for their services on the Board at a rate not to exceed the daily rate at which judges of the United States courts of appeals are compensated. No member may be paid for more than 90 days in any calendar year.\n**(2) Travel expenses**\nEach member shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n##### (f) Chairperson\nThe Chairperson of the Board shall be elected by the members and shall serve for a 2-year term, which may be renewed once by the Board for an additional 2-year term.\n##### (g) Removal of members\nThe members of the Board, by a vote of 13 members, may remove a member from the Board for\u2014\n**(1)**\nmalfeasance in office;\n**(2)**\npersistent neglect of, or inability to discharge, Board duties; or\n**(3)**\nconduct unbecoming of a member of the Board.\n##### (h) Quorum\nA quorum for purposes of conducting Board business shall be a majority of the members of the Board presently serving.\n##### (i) Voting\nAll members of the Board are entitled to vote on any matters coming before the Board unless otherwise provided by rules adopted by the Board concerning voting on matters in which a member has, or appears to have, a financial or other personal interest.\n##### (j) Bylaws\nThe Board shall adopt bylaws governing the operation of the Board, which may include provisions authorizing other officers of the Board and governing proxy voting, telephonic and video meetings, and the appointment of committees.\n##### (k) Duties of the Board\nThe Board shall\u2014\n**(1)**\nappoint a Director of the Office not later than 2 months after the establishment of the Board\u2014\n**(A)**\nwho shall be selected on the basis of training, experience, and other relevant qualifications; and\n**(B)**\nwho shall serve at the pleasure of the Board;\n**(2)**\nconvene a meeting not later than 4 months after the establishment of the Board, and not less frequently than quarterly thereafter;\n**(3)**\nsubmit appropriations requests to Congress for the provision of legal services to individuals represented by counsel in proceedings described in section 292(a) of the Immigration and Nationality Act, as amended by section 101(a);\n**(4)**\nsubmit an annual report to Congress and the President that\u2014\n**(A)**\ndescribes the operation of the Office and the delivery of services required under section 292 of the Immigration and Nationality Act; and\n**(B)**\nincludes\u2014\n**(i)**\nthe number of people who were provided legal services during the reporting period pursuant to such section 292 and the types of proceedings in which such people were represented;\n**(ii)**\nthe custodial status of the people who were represented;\n**(iii)**\naggregate case outcomes for the people who were represented; and\n**(iv)**\nthe status of appointments and vacancies on the Board and Local Boards;\n**(5)**\ncomplete and submit to Congress and to the President every 7 years a comprehensive review and evaluation of the implementation of this Act, including the identification of the resources needed to carry out the requirements under this Act and the amendments made by this Act for the foreseeable future;\n**(6)**\nmake the reports described in paragraphs (4) and (5) publicly available at the time they are submitted to Congress and to the President;\n**(7)**\nestablish and maintain standards for the provision of representation that are consistent with appointed counsel\u2019s duty to provide representation under section 292 of the Immigration and Nationality Act, including\u2014\n**(A)**\nthe minimum experience, skill, performance, and other qualifications for participation as appointed counsel;\n**(B)**\nongoing training, professional development, and mentorship and supervision required to remain eligible to serve as appointed counsel under such section 292;\n**(C)**\nreasonable, manageable, and sustainable appointed counsel caseloads that are consistent with appointed counsel\u2019s primary duty to provide representation to individuals described in such section 292;\n**(D)**\nthe elements to be evaluated during performance reviews of appointed counsel to determine whether they complied with their duty to provide representation under such section 292;\n**(E)**\nhow to provide adequate representation of clients whose cases present conflicts of interest; and\n**(F)**\nensuring continued representation in circumstances in which clients move or are transferred, or where cases are transferred or change venue;\n**(8)**\nevaluate plans submitted by Local Boards for the provision of representation of individuals before U.S. Citizenship and Immigration Services in matters described in section 292 of the Immigration and Nationality Act, after taking into account the ability of such plans to provide such representation, and approve such plans if they meet applicable legal requirements of law and are consistent with the policies of the Office;\n**(9)**\nreview the implementation of plans approved by the Board not less frequently than once every 4 years to ensure that each Local Board complies with the plan approved by the Board;\n**(10)**\nestablish policies and procedures with respect to compensation rates and reimbursement of reasonable expenses for appointed counsel under such section 292 and others providing services related to such representation;\n**(11)**\nestablish procedures to obtain investigators, experts, interpreters, and other providers of defense services necessary for effective representation of individuals who are entitled to counsel under such section 292;\n**(12)**\nestablish procedures for the reimbursement of reasonable expenses of attorneys, investigators, experts, interpreters, and other persons providing representation and related services under such section 292;\n**(13)**\napprove staffing levels and budgets for Immigration Public Defender Organizations;\n**(14)**\napprove staffing levels and budgets for the Office; and\n**(15)**\nestablish a mechanism for the submission, review, resolution, and reporting of complaints from individuals entitled to counsel under such section 292 regarding such representation.\n##### (l) Powers of the Board\nThe Board is authorized\u2014\n**(1)**\nto delegate any of its duties, in whole or in part, to the Director, except for the duties described in paragraphs (1), (7), (13) and (14) of subsection (k);\n**(2)**\nto alter or revoke any such delegation to the Director;\n**(3)**\nto provide to Congress information regarding the immigration system that the Board considers relevant to the purpose of the Office;\n**(4)**\nto authorize studies or reports that relate to the purpose of the Office;\n**(5)**\nto combine Local Boards or divide an area served by a Local Board if the Board determines that such action is necessary to carry out the purposes of this section;\n**(6)**\nto remove, by a vote of at least 13 members, a member or members of a Local Board for malfeasance in office, persistent neglect of or inability to discharge duties, or conduct unbecoming of a member of the Local Board;\n**(7)**\nto seek, accept, and use public grants, private contributions, and voluntary and uncompensated (gratuitous services) to assist the Board in carrying out the purposes of this Act and other services related to such purposes; and\n**(8)**\nto take any other action that is reasonably necessary and not inconsistent with the Act to carry out the purposes of this Act.\n#### 204. Director\n##### (a) Requirements\nThe Director of the Office\u2014\n**(1)**\nshall be a licensed attorney in good standing in any United States jurisdiction at the time of his or her appointment and at all times during his or her service as the Director;\n**(2)**\nshall be experienced in representing people in proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101 of this Act; and\n**(3)**\nmay not be a member of the Board.\n##### (b) Duties\nThe Director shall\u2014\n**(1)**\nappoint and fix the compensation of employees of the Office;\n**(2)**\nestablish a personnel management system for the Office that provides for the appointment, pay, promotion, and assignment of all employees on the basis of merit, but without regard to the provisions of subchapter I of chapter 33 of title 5, United States, Code (relating to appointments in the competitive service) or the provisions of chapter 51 and subchapter III of chapter 53 of such title (relating to classification and General Schedule pay rates);\n**(3)**\nemploy such personnel as may be necessary to advance the purposes of the Office, subject to staffing and budget approval of the Board;\n**(4)**\nprovide an annual report to the Board regarding the activities of the Office;\n**(5)**\nprovide such periodic reports and work product to the Board sufficient for the Board to fulfill its duties under section 203(k);\n**(6)**\nallocate and disburse funds appropriated for legal representation and related services in cases subject to this Act pursuant to rules and procedures established by the Board;\n**(7)**\nenter into contracts to provide or receive services with any public or private agency, group, or individual;\n**(8)**\nappoint a Local Administrator for each region to administer and approve, subject to the policies established by the Board, the payment of funds necessary for Panel Attorney representation, including Panel Attorney compensation, investigators, experts, and other providers of representation services, and any other necessary expenses for effective representation;\n**(9)**\nassist the Board in developing rules and standards for the delivery of services under this Act;\n**(10)**\ncoordinate the services funded by the Office with any Federal, state, county, local, or private programs established to provide legal assistance to persons in cases subject to this Act who are unable to afford representation;\n**(11)**\nconsult with professional bodies concerning improving the administration of legal representation for persons in proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101 of this Act; and\n**(12)**\nperform such other duties as may be assigned by the Board.\n#### 205. Employees\n##### (a) In general\nEmployees of the Office shall be treated as employees of the Federal Government solely for purposes of\u2014\n**(1)**\nsubchapter 1 of chapter 81 of title 5, United States Code (relating to compensation for work injuries);\n**(2)**\nchapter 83 of such title 5 (relating to retirement);\n**(3)**\nchapter 84 of such title 5 (relating to the Federal Employees\u2019 Retirement System);\n**(4)**\nchapter 87 of such title 5 (relating to life insurance); and\n**(5)**\nchapter 89 of such title 5 (relating to health insurance).\n##### (b) Employer contributions\nThe Office shall make contributions on behalf of employees of the Office under the provisions referred to in subsection (a) at the same rates applicable to employees of agencies of the Federal Government.\n##### (c) Thrift Savings Plan\nEmployees of the Office may make an election under section 8351 or 8432 of title 5, United States Code, to participate in the Thrift Savings Plan for Federal employees.\n#### 206. Local immigration representation boards\n##### (a) Establishment\nNot later than 6 months after the establishment of the Board, the Office shall delineate administrative regions throughout the United States and establish a local immigration representation board for each region.\n##### (b) Composition of Local Boards\n**(1) In general**\nSubject to subsection (c), each Local Board shall consist of not fewer than 5 members and not greater than 15 members, who shall initially be selected by the Board after consultation with stakeholders in the Local Board\u2019s region, including immigration legal service providers, community-based organizations, and people who are or have been subject to proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101.\n**(2) Attorneys**\nNot fewer than 50 percent of the members of the Local Board selected pursuant to paragraph (1) shall be\u2014\n**(A)**\nlicensed attorneys with experience in the practice of removal defense; or\n**(B)**\nemployees of community-based organizations providing services to immigrants.\n**(3) Subsequent members**\nAfter the initial members are selected pursuant to paragraph (1), each Local Board shall select its own members in accordance with bylaws that have been approved by the Office.\n##### (c) Qualification of members\n**(1) Experience; commitment**\nMembers of a Local Board shall have\u2014\n**(A)**\nsignificant experience defending cases described in section 292 of the Immigration and Nationality Act, as amended by section 101; and\n**(B)**\ndemonstrated a strong commitment to representation in indigent defense matters.\n**(2) Diversity**\nThe composition of each Local Boards shall reflect the diversity of the population that counsel appointed pursuant to such section 292 are responsible for representing, including diversity of race, gender identity, sexual orientation, immigration experience, and socioeconomic background.\n**(3) Restrictions**\nA member of a Local Board may not\u2014\n**(A)**\nbe an employee of an Immigration Public Defender Organization or Community Defender Organization with a contract to provide representation under such section 292;\n**(B)**\nbe a member of an Attorney Panel referred to in section 207(d);\n**(C)**\nbe a judicial officer of the United States or of a State, territory, district, possession, or commonwealth of the United States;\n**(D)**\nbe employed as a prosecutor, a law enforcement official, or a judicial official, or by a prosecutorial or law enforcement agency; or\n**(E)**\nhave held a position described in subparagraph (D) during the 3-year period immediately preceding his or her appointment to the Board.\n##### (d) Term of members of a Local Board\n**(1) In general**\nMembers of a Local Board shall serve 4-year terms, except that the terms of the initial members shall be staggered so that the term of not more than 50 percent of the members expire during any calendar year.\n**(2) Maximum length of service**\nA person may not serve for more than 9 years on a Local Board.\n**(3) Replacement members**\nA person who is appointed to replace a member who has resigned or was removed shall serve the remainder of the term of such departing person.\n##### (e) Compensation of members of a Local Board\n**(1) In general**\nMembers of any Local Board shall be paid for their service at the daily rate at which judges of the United States courts of appeals are compensated, but may not be paid for more than 90 days of such service in any calendar year.\n**(2) Travel expenses**\nMembers of any Local Board shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n##### (f) Chair of Local Board\nEach Local Board shall elect a member of the Local Board to serve as chair for 2 years, which term shall begin on the date of election. Such chair may be reelected to extend such service for an additional 2-year term.\n##### (g) Removal of member of Local Board\nEach Local Board, by a majority vote of the full membership, may remove a member from the Local Board for\u2014\n**(1)**\nmalfeasance in office;\n**(2)**\npersistent neglect of, or inability to discharge, Local Board duties; or\n**(3)**\nconduct unbecoming of a member of the Local Board.\n##### (h) Quorum of Local Board\nA majority of the full membership of the Local Board shall constitute a quorum for the purpose of conducting business.\n##### (i) Local Board governance\nEach Local Board shall adopt bylaws governing the operation of the Local Board, which may include provisions authorizing other officers of the Local Board and proxy voting.\n##### (j) Dissolution of Local boards\nThe Board, upon a 2/3 vote, may dissolve a Local Board for good cause. Upon dissolution, the Office shall ensure that a new Local Board is established not later than 90 days of dissolution. The new members of the Local Board shall be selected by the majority votes of the Immigration Public Defenders and the Panel Attorney representatives of the district or districts to be served and the Director.\n##### (k) Duties of Local Boards\n**(1) Local plans**\n**(A) In general**\nEach Local Board\u2014\n**(i)**\nnot later than 120 days after the Local Board is established, shall develop and submit to the Office for approval a Local Plan for the provision of representation services for the region served by the Local Board;\n**(ii)**\nshall implement the Local Plan after it has been approved by the Office;\n**(iii)**\nmay modify the Local Plan at any time, subject to the approval of the Office; and\n**(iv)**\nshall modify the Local Plan if so directed by the Office.\n**(B) Components; development**\nEach Local Plan developed pursuant to subparagraph (A)\u2014\n**(i)**\nshall provide for the appointment of counsel in a timely manner in accordance with this Act;\n**(ii)**\nshall be developed in consultation with U.S. Citizenship and Immigration Services to ensure that it adequately encompasses proceedings described in section 292 of the Immigration and Nationality Act that are within the jurisdiction of U.S. Citizenship and Immigration Services;\n**(iii)**\nshall consider the existence of any State, county, or locally funded programs providing representation to people in proceedings described in such section 292;\n**(iv)**\nmay provide grants or reimbursements to jurisdictions with programs described in clause (iii) that provide representation that furthers the purposes of this Act;\n**(v)**\nshall prioritize such grants or reimbursements for State, county, and locally funded programs that provide representation to people involved in a proceeding described in such section 292 without regard to any past interaction with the immigration or criminal legal systems;\n**(vi)**\nmay, in accordance with section 207\u2014\n**(I)**\nestablish 1 or more Immigration Public Defender Organizations; and\n**(II)**\ncontract with 1 or more Community Defender Organizations;\n**(vii)**\nshall provide for the establishment of a panel of private attorneys to provide representation under such section 292, in accordance with section 207 of this Act; and\n**(viii)**\nshall provide a plan for holding community engagement meetings that are open to the public not less frequently than twice during each fiscal year.\n**(C) Local plans with border-based components**\n**(i) In general**\nThe Local Plan for each region that is adjacent to the international border between the United States and Mexico border shall provide for representation to all people subject to a proceeding described in section 292 of the Immigration and Nationality Act, as amended by section 101 of this Act.\n**(ii) Identifying counsel**\nThe Local Board of each region described in clause (i) may utilize the entities specified in section 207 and Attorney of the Day, attorney fellowship, and other models\u2014\n**(I)**\nto provide limited representation to people in proceedings at the border; and\n**(II)**\nto coordinate case transfers and referrals for legal representation for people who are subsequently released from, or transferred within, the custody of the Department of Homeland Security or the Office of Refugee Resettlement.\n**(2) Appointments to immigration representation advisory board**\nIf a Local Plan does not provide for the establishment of an Immigration Public Defender Organization or contracting with a Community Defender Organization in the region, the Local Board shall appoint representatives to the Immigration Representation Advisory Board established under section 210(a).\n**(3) Local administrator**\nEach Local Board shall appoint, subject to the approval of the Office, a Local Administrator and such staff as may be necessary to assist the Local Board in administering the selection and appointment of Panel Attorneys.\n**(4) Immigration public defender**\nIf a Local Plan includes the establishment of 1 or more Immigration Public Defender Organizations, the Local Board shall\u2014\n**(A)**\nselect 1 or more Immigration Public Defenders, who shall serve in accordance with section 207(b), for the region or a portion of the region that will be served by the Local Board;\n**(B)**\nperiodically evaluate the performance of the Immigration Public Defender; and\n**(C)**\nsubmit the results of the evaluations required under subparagraph (B), as directed by the Office.\n**(5) Duties of local administrator**\nEach Local Administrator shall\u2014\n**(A)**\nreview, and certify for payment, all vouchers received from Panel Attorneys to compensate them for\u2014\n**(i)**\ntheir time spent representing clients appointed to them pursuant to section 292 of the Immigration and Nationality Act, as amended by section 101 of this Act; and\n**(ii)**\nthe costs of investigators, experts, interpreters, and other providers of defense services for work performed on behalf of the Panel Attorneys and their clients;\n**(B)**\nauthorize reasonable expenditures for transcripts and the services of paralegals and other legal support personnel, to the extent necessary;\n**(C)**\nprepare, at the direction of the Office, an annual budget for the provision of representation services under such section 292, except for representation services provided by an Immigration Public Defender Office;\n**(D)**\nimplement procedures established by the Office, permitting a Panel Attorney or other representative appointed under such section 292 to appeal a decision of the Local Administrator concerning compensation or reimbursement; and\n**(E)**\nperform other duties related to the authorization, payment, and budgeting of expenses related to Panel Attorneys, as assigned by the Director.\n**(6) Representation of financially eligible persons**\nThe Local Board shall establish procedures for the appointment of counsel for any person who\u2014\n**(A)**\nis subject to a proceeding described in section 292 of the Immigration and Nationality Act, as amended by section 101; and\n**(B)**\nis financially unable to obtain high-quality representation.\n#### 207. Types of immigration defenders\n##### (a) In general\nTo ensure representation of all eligible persons in proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101, the Local Board may\u2014\n**(1)**\nestablish 1 or more Immigration Public Defender Organizations in the region comprising the Local Board's jurisdiction;\n**(2)**\ncontract with existing Community Defender Organizations; and\n**(3)**\nestablish a Panel Attorney system.\n##### (b) Immigration public defender\n**(1) In general**\nAn Immigration Public Defender Organization shall consist of 1or more full-time salaried attorneys. Each Immigration Public Defender Organization shall be supervised by an Immigration Public Defender appointed by the Local Board that established the organization, subject to the approval of the Office and without regard to the provisions of title 5, United States Code, governing appointments in the competitive service.\n**(2) Removal**\n**(A) In general**\nThe Immigration Public Defender shall serve at the pleasure of the Local Board, but may be removed by the Director for\u2014\n**(i)**\nmalfeasance in office;\n**(ii)**\npersistent neglect or inability to discharge the duties of an Immigration Public Defender; or\n**(iii)**\nconduct unbecoming of a representative of the Office.\n**(B) Nonfactors for justifying removal**\nThe efforts and advocacy of an Immigration Public Defender to ensure that the Office carries out its responsibilities under this Act, including ensuring parity of resources, protecting counsel\u2019s duty to provide representation, and ensuring manageable caseloads consistent with that duty, may not serve as a basis for removal or for initiating proceedings for removal against the Immigration Public Defender.\n**(3) Continued service until appointment of successor**\nUpon the expiration of the term of service for which he or she was appointed, an Immigration Public Defender may continue to perform the duties of such office, in accordance with rules established by the Local Board, until the earlier of\u2014\n**(A)**\nthe date on which a successor is appointed; or\n**(B)**\nthe date that is 1 year after the expiration of such term.\n**(4) Compensation**\nThe compensation of each Immigration Public Defender shall be fixed by the Local Board at a rate that is comparable to\u2014\n**(A)**\nthe rate of compensation received by the Principal Legal Advisor of U.S. Immigration and Customs Enforcement who is practicing in the nearest court where representation is furnished; or\n**(B)**\nif more than 1 court is involved, the rate of compensation that is paid to the higher paid Principal Legal Advisor in such courts.\n**(5) Additional personnel**\n**(A) Appointments**\nThe Immigration Public Defender may appoint, without regard to the provisions of title 5, United States Code, governing appointments in the competitive service, full-time attorneys in such number as may be approved by the Office and other personnel in such number as may be approved.\n**(B) Compensation**\nCompensation paid to the attorneys and other personnel approved by the Office pursuant to subparagraph (A) shall be fixed by the Immigration Public Defender at a rate that is comparable to\u2014\n**(i)**\nthe rate of compensation that is paid to attorneys and other personnel of similar qualifications and experience in the Office of the Principal Legal Advisor in the nearest court where representation is furnished; or\n**(ii)**\nif more than 1 court is involved, the rate of compensation that is paid to the higher paid person of similar qualifications and experience in such courts.\n**(6) Treatment as Federal government employees**\nEmployees of an Immigration Public Defender Organization shall be treated as employees of the Federal Government solely for purposes of\u2014\n**(A)**\nsubchapter 1 of chapter 81 of title 5, United States Code (relating to compensation for work injuries);\n**(B)**\nchapter 83 of such title 5 (relating to retirement);\n**(C)**\nchapter 84 of such title 5 (relating to the Federal Employees\u2019 Retirement System);\n**(D)**\nchapter 87 of such title 5 (relating to life insurance); and\n**(E)**\nchapter 89 of such title 5 (relating to health insurance).\n**(7) Restriction**\nAn Immigration Public Defender and any attorney appointed to serve in an Immigration Public Defender Organization is prohibited from engaging in the private practice of law.\n**(8) Limited liability**\nThe Office, to the extent the Director considers appropriate, shall provide representation for and hold harmless, or provide liability insurance for, any person who is an officer or employee of an Immigration Public Defender Organization.\n**(9) Reports**\nEach Immigration Public Defender Organization shall submit periodic reports of its activities and financial positions and its proposed budget to the Local Board at the times and in the form prescribed by the Local Board.\n##### (c) Community Defender Organizations\n**(1) In general**\nA Community Defender Organization shall be a nonprofit legal representation service established and administered by any group authorized by the Local Plan to provide representation to individuals subject to proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101.\n**(2) Annual report**\nEach Community Defender Organization shall submit an annual report to the Local Board that sets forth its activities during the previous fiscal year and the anticipated caseload and expenses for the upcoming fiscal year.\n##### (d) Attorney Panel\nEach Local Plan developed pursuant to section 206(k)(1) shall provide for\u2014\n**(1)**\nthe appointment of qualified private attorneys from an Attorney Panel within the region;\n**(2)**\nthe implementation of standards established by the Office setting forth the minimum qualifications for Panel Attorneys; and\n**(3)**\nthe establishment of a system to ensure that\u2014\n**(A)**\nthe number of attorneys on each Attorney Panel is limited to provide each attorney with sufficient appointments to maintain continuing familiarity with immigration law and procedure;\n**(B)**\nthere is early entry of counsel, including representation as soon as possible in all proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101;\n**(C)**\nthere are adequate support services, including training and technical support, for members of each Attorney Panel for every area in the region;\n**(D)**\nconflicts of interests are avoided; and\n**(E)**\nthere is equal employment opportunity for the employees of Immigration Public Defender Organizations and Panel Attorneys.\n#### 208. Compensation and reimbursement of expenses of counsel\n##### (a) In general\nThe Office shall establish the appropriate hourly rates and salaries to be paid to counsel appointed under each Local Plan, which\u2014\n**(1)**\nshall be established at levels that will ensure the provision of high-quality legal representation for all people represented in proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101; and\n**(2)**\nshall be calculated to provide appointed counsel with compensation that is comparable to the compensation paid to\u2014\n**(A)**\nattorneys who are employed by the Office of the Principal Legal Advisor of U.S. Immigration and Customs Enforcement nearest to the forum in which such counsel is providing representation;\n**(B)**\nattorneys employed by the corresponding Federal prosecutor\u2019s office; or\n**(C)**\nany other attorney representing the Government in connection with proceedings that are comparable to proceedings described in such section 292.\n##### (b) Use of billing caps\nIf the Office places caps on total billing for legal representation, the Office shall establish policies and procedures for counsel to request authorization to exceed such caps to the extent required to ensure effective representation.\n##### (c) Fees; additional compensation\nThe Office shall establish\u2014\n**(1)**\ndistinct fees to apply to counsel providing services in proceedings that fall within the geographic jurisdiction of each of the United States courts of appeal within each region delineated by the Office pursuant to section 206(a), after taking into account the prevailing wage rates for qualified attorneys within the geographic area in which representation will be provided under section 292 of the Immigration and Nationality Act, as amended by section 101; and\n**(2)**\nadditional compensation to be paid to counsel who provide representation under such section 292 to individuals in remote and underserved areas, after taking into account the distance from the place of business of such counsel to\u2014\n**(A)**\nthe immigration courts;\n**(B)**\nDepartment of Homeland Security and Department of Health and Human Services facilities; and\n**(C)**\nother relevant sites where such representation is expected to be provided.\n##### (d) Reimbursement for expenses; salary increases\n**(1) Reimbursements**\nCounsel providing representation under section 292 of the Immigration and Nationality Act, as amended by section 101, shall be reimbursed by the Department of Homeland Security for expenses reasonably incurred in the course of such representation, including the costs of transcripts, but may not be reimbursed by the Federal Government for expenses related to defending against malpractice claims.\n**(2) Salary increases**\nThe Office shall establish policies and procedures governing increases in hourly rates, salaries, and fees initially determined under subsection (a) or (c).\n##### (e) Payments in excess of established fees\nThe Office shall establish policies and procedures for requesting and approving payments in excess of the fees established under subsection (c) for extended or complex representation if such excess payments are necessary to provide fair compensation for the counsel providing such representation.\n#### 209. Services other than counsel\n##### (a) Services To be preapproved by the Local Board\n**(1) In general**\nCounsel appointed to represent individuals in proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101, may request approval from the Local Board for investigative, expert, or other services necessary for such representation pursuant to procedures established by the Board, including services necessary to develop release plans and provide post-release services for people in the custody of the Department of Homeland Security or the Office of Refugee Resettlement.\n**(2) Examples of services**\nServices subject to preapproval under paragraph (1) may include\u2014\n**(A)**\nthe retention of specialized counsel in connection with ancillary matters appropriate to such proceedings;\n**(B)**\nservices and support related to mental health, housing, addiction, food, travel, and accompaniment to immigration court proceedings;\n**(C)**\ncopying or obtaining discovery materials that are in the possession, custody, or control of the Government; or\n**(D)**\nany other services required to ensure effective representation or the interests of justice.\n##### (b) Services To be approved by the Local Board after the fact\n**(1) In general**\nCounsel appointed to represent individuals in proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101, may obtain, without prior authorization, but subject to later review by the Local Board, investigative, expert, and other services if necessary for representation.\n**(2) Payment**\nIn the interests of justice and upon a determination by the Local Board that timely procurement of certain necessary services could not await prior authorization, payment for such services may be approved by the Local Board after they have been obtained.\n##### (c) Amount of compensation\nIn determining the appropriate compensation for services other than counsel, the Office shall ensure that such compensation is comparable to the compensation paid to the Government for substantially similar services.\n##### (d) Policies and procedures\nThe Office shall establish policies and procedures that\u2014\n**(1)**\nidentify the circumstances under which\u2014\n**(A)**\npayment shall be made for services other than counsel; and\n**(B)**\nprior authorization for certain necessary services is not required; and\n**(2)**\npermit counsel appointed to represent individuals in proceedings described in section 292 of the Immigration and Nationality Act, as amended by section 101, to seek increases in funding for such services if counsel reasonably believes that the compensation established by the Office pursuant to subsection (c) does not meet the parity requirement under such subsection.\n##### (e) Financial eligibility determinations\n**(1) In general**\nPrivate counsel for any person who is financially unable to obtain services other than counsel necessary for representation, including services described in subsections (a) and (b), may request that the Local Administrator make a determination of the financial eligibility for such person to receive Government funding for such services.\n**(2) Payment**\nIf the Local Administrator determines that a person described in paragraph (1) is financially unable to obtain necessary services other than counsel, the Local Administrator shall authorize payment for such services pursuant to procedures established by the Office.\n#### 210. Immigration Representation Advisory Board\n##### (a) Establishment\n**(1) In general**\nSubject to paragraph (2), there is established the Immigration Representation Advisory Board, which shall consist of\u2014\n**(A)**\n1 Immigration Public Defender representative from each region delineated pursuant to section 206(a), who shall be selected by the Immigration Public Defenders within each such region;\n**(B)**\n1 Community Defender Organization representative from each region delineated pursuant to section 206(a), who shall be selected by the Community Defender Organizations within each such region; and\n**(C)**\n1 Panel Attorney representative from within the jurisdiction of each Federal circuit court of appeals, who shall be selected by the Panel Attorneys within each such circuit.\n**(2) Alternative selection process**\n**(A) No immigration public defender office**\nIf a Local Plan does not provide for the establishment of an Immigration Public Defender Office, the relevant Local Board shall appoint 2 Community Defender Organization representatives to serve on the Immigration Representation Advisory Board.\n**(B) No community defender organization**\nIf a Local Plan does not provide for a contract with a Community Defender Organization, the relevant Local Board shall appoint 2 Immigration Public Defender Representatives to serve on the Immigration Representation Advisory Board.\n##### (b) Term of service\n**(1) In general**\nMembers of the Immigration Representation Advisory Board shall serve 2-year terms, except that the terms of 50 percent of the initial members appointed pursuant to subsection (a) shall be 1 year.\n**(2) Maximum consecutive service**\nNo member may serve on the Immigration Representation Advisory Board for more than 6 consecutive years.\n**(3) Partial term appointments**\nIf a member of the Immigration Representation Advisory Board does not serve until the end of his or her term due to resignation or removal, the person appointed to replace such member shall serve for the remainder of such term.\n##### (c) Compensation\nMembers of the Immigration Representation Advisory Board shall serve without compensation, but shall be reimbursed for all actual and necessary expenses reasonably incurred in the performance of their duties as members of the Immigration Representation Advisory Board.\n##### (d) Governance; meetings\nThe Immigration Representation Advisory Board shall\u2014\n**(1)**\nestablish bylaws;\n**(2)**\nselect a chairperson from among its members;\n**(3)**\nappoint other such officers as it deems necessary; and\n**(4)**\nmeet not less frequently than once each year.\nIII\nAuthorization of appropriations\n#### 301. Authorization of appropriations\n##### (a) In general\nThere are authorized to be appropriated to the Office of Immigration Representation, out of any money in the Treasury that is not otherwise appropriated, such sums as may be necessary to carry out this Act, and the amendments made by this Act, including\u2014\n**(1)**\nestablishing and operating the Office; and\n**(2)**\nproviding continuing education and training of counsel providing representation under section 292 of the Immigration and Nationality Act, as amended by section 101.\n##### (b) Availability of funds\nIf so specified in appropriation Acts, amounts appropriated pursuant to subsection (a) shall remain available until expended. Payments from such appropriations shall be made under the supervision of the Director of the Office of Immigration Representation.\n#### 302. Minimum funding for the Office of Immigration Representation\n##### (a) In general\nThe amount appropriated to the Office of Immigration Representation for each fiscal year shall be not less than the amount equal to the sum of the combined amount appropriated for Federal immigration enforcement and prosecution agencies and the Office, multiplied by the prosecution-defense ratio calculated pursuant to subsection (b).\n##### (b) Calculation of prosecution-Defense ratio\n**(1) In general**\nExcept as provided in paragraph (2), the Office of Management and Budget shall calculate the prosecution-defense ratio, for purposes of subsection (a), by dividing the sum appropriated to the Office of Immigration Representation account for the most recently concluded fiscal year by the combined amount appropriated for such fiscal year for Federal immigration enforcement and prosecution agencies, including amounts appropriated for\u2014\n**(A)**\nU.S. Immigration and Customs Enforcement;\n**(B)**\nU.S. Customs and Border Protection; and\n**(C)**\nthe Office of Immigration Litigation of the Department of Justice.\n**(2) Effect of shifting prosecutorial functions**\nIf the law enforcement or prosecutorial functions of the agencies or offices referred to in subparagraphs (A) through (C) of paragraph (1) on the date of the enactment of this Act are performed by different agencies or offices in a future fiscal year, the Office of Management and Budget shall use the amount appropriated for those functions in calculating the prosecution-defense ratio under paragraph (1).",
      "versionDate": "2025-04-30",
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
        "name": "Immigration",
        "updateDate": "2025-05-20T14:47:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
    "originChamber": "House",
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
          "measure-id": "id119hr3127",
          "measure-number": "3127",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-30",
          "originChamber": "HOUSE",
          "update-date": "2026-03-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3127v00",
            "update-date": "2026-03-09"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fairness to Freedom Act of 2025</strong></p><p>This bill establishes a right to legal representation in certain immigration proceedings (e.g., removal and immigration bond hearings) at the government's expense for individuals who cannot afford representation. The bill also establishes various entities to facilitate such legal representation.</p><p>Currently, individuals in these immigration proceedings may be represented by counsel but not at government expense.</p><p>The bill addresses various issues related to such legal representation, including (1) the scope of the representation, (2) criteria for determining whether the individual is financially unable to afford representation, and (3) requirements relating to allowing the individual to meet with their lawyer and receiving relevant documents. Immigration proceedings may not commence until counsel has been appointed.</p><p>The bill also establishes the Office of Immigration Representation to ensure that qualified individuals who cannot afford legal representation receive the representation as required by this bill. The office's duties shall include establishing (1) administrative regions throughout the United States, and (2) a local immigration representation board for each region.</p><p>The local boards must, subject to the office's approval, develop and implement plans for providing legal representation under this bill. To provide such legal representation, the local boards may (1) establish one or more immigrant public defender organizations, (2) contract with existing community defender organizations, and (3) establish a panel attorney system.</p><p>The bill establishes minimum funding requirements for the office.</p>"
        },
        "title": "Fairness to Freedom Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3127.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fairness to Freedom Act of 2025</strong></p><p>This bill establishes a right to legal representation in certain immigration proceedings (e.g., removal and immigration bond hearings) at the government's expense for individuals who cannot afford representation. The bill also establishes various entities to facilitate such legal representation.</p><p>Currently, individuals in these immigration proceedings may be represented by counsel but not at government expense.</p><p>The bill addresses various issues related to such legal representation, including (1) the scope of the representation, (2) criteria for determining whether the individual is financially unable to afford representation, and (3) requirements relating to allowing the individual to meet with their lawyer and receiving relevant documents. Immigration proceedings may not commence until counsel has been appointed.</p><p>The bill also establishes the Office of Immigration Representation to ensure that qualified individuals who cannot afford legal representation receive the representation as required by this bill. The office's duties shall include establishing (1) administrative regions throughout the United States, and (2) a local immigration representation board for each region.</p><p>The local boards must, subject to the office's approval, develop and implement plans for providing legal representation under this bill. To provide such legal representation, the local boards may (1) establish one or more immigrant public defender organizations, (2) contract with existing community defender organizations, and (3) establish a panel attorney system.</p><p>The bill establishes minimum funding requirements for the office.</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119hr3127"
    },
    "title": "Fairness to Freedom Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fairness to Freedom Act of 2025</strong></p><p>This bill establishes a right to legal representation in certain immigration proceedings (e.g., removal and immigration bond hearings) at the government's expense for individuals who cannot afford representation. The bill also establishes various entities to facilitate such legal representation.</p><p>Currently, individuals in these immigration proceedings may be represented by counsel but not at government expense.</p><p>The bill addresses various issues related to such legal representation, including (1) the scope of the representation, (2) criteria for determining whether the individual is financially unable to afford representation, and (3) requirements relating to allowing the individual to meet with their lawyer and receiving relevant documents. Immigration proceedings may not commence until counsel has been appointed.</p><p>The bill also establishes the Office of Immigration Representation to ensure that qualified individuals who cannot afford legal representation receive the representation as required by this bill. The office's duties shall include establishing (1) administrative regions throughout the United States, and (2) a local immigration representation board for each region.</p><p>The local boards must, subject to the office's approval, develop and implement plans for providing legal representation under this bill. To provide such legal representation, the local boards may (1) establish one or more immigrant public defender organizations, (2) contract with existing community defender organizations, and (3) establish a panel attorney system.</p><p>The bill establishes minimum funding requirements for the office.</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119hr3127"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3127ih.xml"
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
      "title": "Fairness to Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fairness to Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the right to counsel, at Government expense for those who cannot afford counsel, for people facing removal.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:48:32Z"
    }
  ]
}
```
