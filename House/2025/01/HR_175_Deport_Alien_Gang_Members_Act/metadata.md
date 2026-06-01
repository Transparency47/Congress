# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/175?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/175
- Title: Deport Alien Gang Members Act
- Congress: 119
- Bill type: HR
- Bill number: 175
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-04-07T15:34:14Z
- Update date including text: 2025-04-07T15:34:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/175",
    "number": "175",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Deport Alien Gang Members Act",
    "type": "HR",
    "updateDate": "2025-04-07T15:34:14Z",
    "updateDateIncludingText": "2025-04-07T15:34:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:23:05Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NY"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "WY"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "OK"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "AL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "MD"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MN"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MS"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WI"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MN"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "SC"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "KS"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "CO"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr175ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 175\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. McClintock (for himself, Mr. Weber of Texas , Ms. Tenney , Mr. Nehls , Ms. Hageman , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act with respect to aliens associated with criminal gangs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deport Alien Gang Members Act .\n#### 2. Grounds of inadmissibility and deportability for alien gang members\n##### (a) Definition of gang member\nSection 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ) is amended by adding at the end the following:\n(53) The term criminal gang means an ongoing group, club, organization, or association of 5 or more persons that has as 1 of its primary purposes the commission of 1 or more of the offenses described in this paragraph and the members of which engage, or have engaged within the past 5 years, in a continuing series of such offenses, or that has been designated as a criminal gang by the Secretary of Homeland Security, in consultation with the Attorney General, as meeting these criteria. The offenses described, whether committed, in whole or in part, within or outside of the United States and regardless of whether the offenses occurred before, on, or after the date of the enactment of this paragraph, are the following: (A) A Federal, State, local, or Tribal offense that is punishable by imprisonment for more than 1 year and relates to a controlled substance (as so classified under the relevant Federal, State, local, or Tribal law), regardless of whether the substance is classified as a controlled substance under section 102 of the Controlled Substances Act ( 21 U.S.C. 802 ). (B) A foreign offense that is punishable by imprisonment for more than 1 year and relates to a controlled substance as defined under section 102 of the Controlled Substances Act ( 21 U.S.C. 802 ). (C) An offense that is punishable by imprisonment for more than 1 year and involves firearms or explosives (as defined under the relevant Federal, State, local, Tribal, or foreign law) or in violation of section 931 of title 18, United States Code (relating to purchase, ownership, or possession of body armor by violent felons). (D) An offense under section 274 (relating to bringing in and harboring certain aliens), section 277 (relating to aiding or assisting certain aliens to enter the United States), or section 278 (relating to importation of alien for immoral purpose). (E) A crime of violence (as defined in section 16(a) of title 18, United States Code). (F) A crime involving obstruction of justice, tampering with or retaliating against a witness, victim, or informant, or burglary (as such terms are defined under the relevant Federal, State, local, Tribal, or foreign law). (G) Any conduct punishable under sections 1028, 1028A, and 1029 of title 18, United States Code (relating to fraud, aggravated identity theft or fraud and related activity in connection with identification documents or access devices), sections 1581 through 1594 of such title (relating to peonage, slavery, and trafficking in persons), section 1951 of such title (relating to interference with commerce by threats or violence), section 1952 of such title (relating to interstate and foreign travel or transportation in aid of racketeering enterprises), section 1956 of such title (relating to the laundering of monetary instruments), section 1957 of such title (relating to engaging in monetary transactions in property derived from specified unlawful activity), or sections 2312 through 2315 of such title (relating to interstate transportation of stolen motor vehicles or stolen property). (H) A conspiracy to commit an offense described in subparagraphs (A) through (G). .\n##### (b) Inadmissibility\nSection 212(a)(2) of such Act ( 8 U.S.C. 1182(a)(2) ) is amended by adding at the end the following:\n(J) Aliens associated with criminal gangs Any alien is inadmissible who a consular officer, an immigration officer, the Secretary of Homeland Security, or the Attorney General knows, or has reason to believe\u2014 (i) is, or has been, a member of a criminal gang; (ii) has promoted, conspired with, aided, or participated in the activities of a criminal gang, whether within or outside of the United States; or (iii) seeks to enter the United States, or has entered the United States, in furtherance of the activities of a criminal gang, whether those activities take place within or outside of the United States. .\n##### (c) Deportability\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended by adding at the end the following:\n(G) Aliens associated with criminal gangs Any alien is deportable who\u2014 (i) is or has been a member of a criminal gang; or (ii) has promoted, conspired with, aided, or participated in the activities of a criminal gang, whether within or outside of the United States. .\n##### (d) Designation\n**(1) In general**\nChapter 2 of title II of the Immigration and Nationality Act ( 8 U.S.C. 1182 ) is amended by inserting after section 219 the following:\nSec. 220. Designation of criminal gang. (a) Designation (1) In general The Secretary of Homeland Security, in consultation with the Attorney General, may designate a group, club, organization, or association of 5 or more persons as a criminal gang if the Secretary finds that their conduct is described in section 101(a)(53). (2) Procedure (A) Notification 7 days before making a designation under this subsection, the Secretary shall, by classified communication, notify the Speaker and minority leader of the House of Representatives, the president pro tempore, majority leader, and minority leader of the Senate, and the members of the relevant committees of the House of Representatives and the Senate, in writing, of the intent to designate a group, club, organization, or association of 5 or more persons under this subsection and the factual basis therefor. (B) Publication in the Federal Register The Secretary shall publish the designation in the Federal Register 7 days after providing the notification under subparagraph (A). (3) Record (A) In general In making a designation under this subsection, the Secretary shall create an administrative record. (B) Classified information The Secretary may consider classified information in making a designation under this subsection. Classified information shall not be subject to disclosure for such time as it remains classified, except that such information may be disclosed to a court ex parte and in camera for purposes of judicial review under subsection (c). (4) Period of designation (A) In general A designation under this subsection shall be effective for all purposes until revoked under paragraph (5) or (6) or set aside pursuant to subsection (c). (B) Review of designation upon petition (i) In general The Secretary shall review the designation of a criminal gang under the procedures set forth in clauses (iii) and (iv) if the designated group, club, organization, or association of 5 or more persons files a petition for revocation within the petition period described in clause (ii). (ii) Petition period For purposes of clause (i)\u2014 (I) if the designated group, club, organization, or association of 5 or more persons has not previously filed a petition for revocation under this subparagraph, the petition period begins 2 years after the date on which the designation was made; or (II) if the designated group, club, organization, or association of 5 or more persons has previously filed a petition for revocation under this subparagraph, the petition period begins 2 years after the date of the determination made under clause (iv) on that petition. (iii) Procedures Any group, club, organization, or association of 5 or more persons that submits a petition for revocation under this subparagraph of its designation as a criminal gang must provide evidence in that petition that it is not described in section 101(a)(53). (iv) Determination (I) In general Not later than 30 days after receiving a petition for revocation submitted under this subparagraph, the Secretary shall make a determination as to such revocation. (II) Classified information The Secretary may consider classified information in making a determination in response to a petition for revocation. Classified information shall not be subject to disclosure for such time as it remains classified, except that such information may be disclosed to a court ex parte and in camera for purposes of judicial review under subsection (c). (III) Publication of determination A determination made by the Secretary under this clause shall be published in the Federal Register. (IV) Procedures Any revocation by the Secretary shall be made in accordance with paragraph (6). (C) Other review of designation (i) In general If in a 5-year period no review has taken place under subparagraph (B), the Secretary shall review the designation of the criminal gang in order to determine whether such designation should be revoked pursuant to paragraph (6). (ii) Procedures If a review does not take place pursuant to subparagraph (B) in response to a petition for revocation that is filed in accordance with that subparagraph, then the review shall be conducted pursuant to procedures established by the Secretary. The results of such review and the applicable procedures shall not be reviewable in any court. (iii) Publication of results of review The Secretary shall publish any determination made pursuant to this subparagraph in the Federal Register. (5) Revocation by act of Congress The Congress, by an Act of Congress, may block or revoke a designation made under paragraph (1). (6) Revocation based on change in circumstances (A) In general The Secretary may revoke a designation made under paragraph (1) at any time, and shall revoke a designation upon completion of a review conducted pursuant to subparagraphs (B) and (C) of paragraph (4) if the Secretary finds that\u2014 (i) the group, club, organization, or association of 5 or more persons that has been designated as a criminal gang is no longer described in section 101(a)(53); or (ii) the national security or the law enforcement interests of the United States warrants a revocation. (B) Procedure The procedural requirements of paragraphs (2) and (3) shall apply to a revocation under this paragraph. Any revocation shall take effect on the date specified in the revocation or upon publication in the Federal Register if no effective date is specified. (7) Effect of revocation The revocation of a designation under paragraph (5) or (6) shall not affect any action or proceeding based on conduct committed prior to the effective date of such revocation. (8) Use of designation in trial or hearing If a designation under this subsection has become effective under paragraph (2) an alien in a removal proceeding shall not be permitted to raise any question concerning the validity of the issuance of such designation as a defense or an objection. (b) Amendments to a designation (1) In general The Secretary may amend a designation under this subsection if the Secretary finds that the group, club, organization, or association of 5 or more persons has changed its name, adopted a new alias, dissolved and then reconstituted itself under a different name or names, or merged with another group, club, organization, or association of 5 or more persons. (2) Procedure Amendments made to a designation in accordance with paragraph (1) shall be effective upon publication in the Federal Register. Paragraphs (2), (4), (5), (6), (7), and (8) of subsection (a) shall also apply to an amended designation. (3) Administrative record The administrative record shall be corrected to include the amendments as well as any additional relevant information that supports those amendments. (4) Classified information The Secretary may consider classified information in amending a designation in accordance with this subsection. Classified information shall not be subject to disclosure for such time as it remains classified, except that such information may be disclosed to a court ex parte and in camera for purposes of judicial review under subsection (c) of this section. (c) Judicial review of designation (1) In general Not later than 30 days after publication in the Federal Register of a designation, an amended designation, or a determination in response to a petition for revocation, the designated group, club, organization, or association of 5 or more persons may seek judicial review in the United States Court of Appeals for the District of Columbia Circuit. (2) Basis of review Review under this subsection shall be based solely upon the administrative record, except that the Government may submit, for ex parte and in camera review, classified information used in making the designation, amended designation, or determination in response to a petition for revocation. (3) Scope of review The Court shall hold unlawful and set aside a designation, amended designation, or determination in response to a petition for revocation the court finds to be\u2014 (A) arbitrary, capricious, an abuse of discretion, or otherwise not in accordance with law; (B) contrary to constitutional right, power, privilege, or immunity; (C) in excess of statutory jurisdiction, authority, or limitation, or short of statutory right; (D) lacking substantial support in the administrative record taken as a whole or in classified information submitted to the court under paragraph (2); or (E) not in accord with the procedures required by law. (4) Judicial review invoked The pendency of an action for judicial review of a designation, amended designation, or determination in response to a petition for revocation shall not affect the application of this section, unless the court issues a final order setting aside the designation, amended designation, or determination in response to a petition for revocation. (5) Expedited review It shall be the duty of the Court to advance on the docket and expedite to the greatest possible extent the disposition of any case considered under this subsection. (d) Definitions As used in this section\u2014 (1) the term classified information has the meaning given that term in section 1(a) of the Classified Information Procedures Act (18 U.S.C. App.); (2) the term national security means the national defense, foreign relations, or economic interests of the United States; (3) the term relevant committees means the Committees on the Judiciary of the Senate and of the House of Representatives; and (4) the term Secretary means the Secretary of Homeland Security, in consultation with the Attorney General. .\n**(2) Clerical amendment**\nThe table of contents for such Act is amended by inserting after the item relating to section 219 the following:\nSec. 220. Designation. .\n##### (e) Mandatory detention of criminal gang members\n**(1) In general**\nSection 236(c)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c)(1) ) is amended\u2014\n**(A)**\nin subparagraph (C), by striking or at the end;\n**(B)**\nin subparagraph (D), by inserting or at the end; and\n**(C)**\nby inserting after subparagraph (D) the following:\n(E) is inadmissible under section 212(a)(2)(J) or deportable under section 217(a)(2)(G), .\n**(2) Annual report**\nNot later than March 1 of each year (beginning 1 year after the date of the enactment of this Act), the Secretary of Homeland Security, after consultation with the appropriate Federal agencies, shall submit a report to the Committees on the Judiciary of the House of Representatives and of the Senate on the number of aliens detained under the amendments made by paragraph (1).\n##### (f) Claims based on gang affiliation\n**(1) Inapplicability of restriction on removal to certain countries**\nSection 241(b)(3)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1251(b)(3)(B) ) is amended, in the matter preceding clause (i), by inserting who is described in section 212(a)(2)(J)(i) or section 237(a)(2)(G)(i) or who is after to an alien .\n**(2) Ineligibility for asylum**\nSection 208(b)(2)(A) of such Act ( 8 U.S.C. 1158(b)(2)(A) ) (as amended by section 201 of this Act) is further amended\u2014\n**(A)**\nin clause (v), by striking or at the end;\n**(B)**\nby redesignating clause (vi) as clause (vii); and\n**(C)**\nby inserting after clause (v) the following:\n(vi) the alien is described in section 212(a)(2)(J)(i) or section 237(a)(2)(G)(i); or .\n##### (g) Temporary protected status\nSection 244 of such Act ( 8 U.S.C. 1254a ) is amended\u2014\n**(1)**\nby striking Attorney General each place it appears and inserting Secretary of Homeland Security ;\n**(2)**\nin subparagraph (c)(2)(B)\u2014\n**(A)**\nin clause (i), by striking or at the end;\n**(B)**\nin clause (ii), by striking the period and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(iii) the alien is, or at any time has been, described in section 212(a)(2)(J) or section 237(a)(2)(G). ; and\n**(3)**\nin subsection (d)\u2014\n**(A)**\nby striking paragraph (3); and\n**(B)**\nin paragraph (4), by adding at the end the following: The Secretary of Homeland Security may detain an alien provided temporary protected status under this section whenever appropriate under any other provision of law. .\n##### (h) Special immigrant juvenile visas\nSection 101(a)(27)(J)(iii) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27)(J)(iii) ) is amended\u2014\n**(1)**\nin subclause (I), by striking and ;\n**(2)**\nin subclause (II), by adding and at the end; and\n**(3)**\nby adding at the end the following:\n(III) no alien who is, or at any time has been, described in section 212(a)(2)(J) or section 237(a)(2)(G) shall be eligible for any immigration benefit under this subparagraph; .\n##### (i) Parole\nAn alien described in section 212(a)(2)(J) of the Immigration and Nationality Act, as added by subsection (b), shall not be eligible for parole under section 212(d)(5)(A) of such Act unless\u2014\n**(1)**\nthe alien is assisting or has assisted the United States Government in a law enforcement matter, including a criminal investigation; and\n**(2)**\nthe alien\u2019s presence in the United States is required by the Government with respect to such assistance.\n##### (j) Ineligibility for other relief\nAn alien described in section 212(a)(2)(J) or 237(a)(2)(G) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2)(J) or 1227(a)(2)(G)) shall be ineligible for any other relief under the immigration laws, including under section 2242 of the Omnibus Consolidated and Emergency Supplemental Appropriations Act, 1999 (and any regulations issued pursuant to such section).\n##### (k) Effective date\nThe amendments made by this section shall take effect on the date of the enactment of this Act and shall apply to acts that occur before, on, or after the date of the enactment of this Act.",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1050",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Criminal Alien Gang Member Removal Act",
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
        "name": "Immigration",
        "updateDate": "2025-02-03T14:52:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr175",
          "measure-number": "175",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr175v00",
            "update-date": "2025-02-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Deport Alien Gang Members Act</strong></p><p>This bill makes non-U.S. nationals (<em>aliens</em> under federal law) associated with criminal gangs inadmissible for entry into the United States and deportable. The bill also establishes procedures to designate groups as criminal gangs.</p><p>An individual shall be inadmissible if certain officers or agencies know or have reason to believe that the individual is or was a criminal gang member or has participated or aided such a group's illegal activities. An individual who is or was a member of such a gang, has participated or aided such a group's illegal activities,\u00a0or seeks to enter or has entered the United States in furtherance of such activity\u00a0shall be deportable.</p><p>Such individuals must be subject to mandatory detention. Furthermore, such individuals shall not be eligible for (1) asylum; (2) temporary protected status; (3) special immigrant juvenile visas; or (4) parole, unless they are assisting the government in a law enforcement matter.</p><p>The bill defines a criminal gang as a group of five or more persons (1) where one of its primary purposes is committing specified criminal offenses and its members have engaged in a continuing series of such offenses within the past five years, or (2) that has been designated as a criminal gang by the Department of Homeland Security\u00a0(DHS).</p><p>The bill also establishes procedures for DHS to designate a group as a criminal gang, including notifying Congress, publishing a notice in the Federal Register, and providing an opportunity for the group to petition for review of the designation.</p>"
        },
        "title": "Deport Alien Gang Members Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr175.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Deport Alien Gang Members Act</strong></p><p>This bill makes non-U.S. nationals (<em>aliens</em> under federal law) associated with criminal gangs inadmissible for entry into the United States and deportable. The bill also establishes procedures to designate groups as criminal gangs.</p><p>An individual shall be inadmissible if certain officers or agencies know or have reason to believe that the individual is or was a criminal gang member or has participated or aided such a group's illegal activities. An individual who is or was a member of such a gang, has participated or aided such a group's illegal activities,\u00a0or seeks to enter or has entered the United States in furtherance of such activity\u00a0shall be deportable.</p><p>Such individuals must be subject to mandatory detention. Furthermore, such individuals shall not be eligible for (1) asylum; (2) temporary protected status; (3) special immigrant juvenile visas; or (4) parole, unless they are assisting the government in a law enforcement matter.</p><p>The bill defines a criminal gang as a group of five or more persons (1) where one of its primary purposes is committing specified criminal offenses and its members have engaged in a continuing series of such offenses within the past five years, or (2) that has been designated as a criminal gang by the Department of Homeland Security\u00a0(DHS).</p><p>The bill also establishes procedures for DHS to designate a group as a criminal gang, including notifying Congress, publishing a notice in the Federal Register, and providing an opportunity for the group to petition for review of the designation.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr175"
    },
    "title": "Deport Alien Gang Members Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Deport Alien Gang Members Act</strong></p><p>This bill makes non-U.S. nationals (<em>aliens</em> under federal law) associated with criminal gangs inadmissible for entry into the United States and deportable. The bill also establishes procedures to designate groups as criminal gangs.</p><p>An individual shall be inadmissible if certain officers or agencies know or have reason to believe that the individual is or was a criminal gang member or has participated or aided such a group's illegal activities. An individual who is or was a member of such a gang, has participated or aided such a group's illegal activities,\u00a0or seeks to enter or has entered the United States in furtherance of such activity\u00a0shall be deportable.</p><p>Such individuals must be subject to mandatory detention. Furthermore, such individuals shall not be eligible for (1) asylum; (2) temporary protected status; (3) special immigrant juvenile visas; or (4) parole, unless they are assisting the government in a law enforcement matter.</p><p>The bill defines a criminal gang as a group of five or more persons (1) where one of its primary purposes is committing specified criminal offenses and its members have engaged in a continuing series of such offenses within the past five years, or (2) that has been designated as a criminal gang by the Department of Homeland Security\u00a0(DHS).</p><p>The bill also establishes procedures for DHS to designate a group as a criminal gang, including notifying Congress, publishing a notice in the Federal Register, and providing an opportunity for the group to petition for review of the designation.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr175"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr175ih.xml"
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
      "title": "Deport Alien Gang Members Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deport Alien Gang Members Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T10:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act with respect to aliens associated with criminal gangs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T10:03:22Z"
    }
  ]
}
```
