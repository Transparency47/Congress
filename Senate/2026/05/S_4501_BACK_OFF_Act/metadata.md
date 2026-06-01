# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4501?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4501
- Title: BACK OFF Act
- Congress: 119
- Bill type: S
- Bill number: 4501
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-28T14:48:49Z
- Update date including text: 2026-05-28T14:48:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S2239-2240)
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S2239-2240)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4501",
    "number": "4501",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "BACK OFF Act",
    "type": "S",
    "updateDate": "2026-05-28T14:48:49Z",
    "updateDateIncludingText": "2026-05-28T14:48:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S2239-2240)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T19:21:56Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4501is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4501\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mr. Cornyn introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo bar aliens from admission to the United States to give birth on United States soil or remaining in the United States to undermine the sovereignty of the United States through birth tourism.\n#### 1. Short titles\nThis Act may be cited as the Barring American Citizenship by Keeping Out Foreign Fraudsters or the BACK OFF Act .\n#### 2. Grounds for inadmissibility to, and removal from the United States for engaging in birth tourism\n##### (a) Grounds of inadmissibility\nSection 212(a)(2)(F) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2)(F) ) is amended to read as follows:\n(F) Aliens undermining the sovereignty of United States through birth tourism (i) In general Any alien convicted of, who admits to having committed, or who admits committing acts which constitute the essential elements of, an offense described in section 274E, 274F, or 275(e) or an offense described in section 1546A of title 18, United States Code, is inadmissible. (ii) Birth tourism An alien is inadmissible if such alien\u2014 (I) (aa) is not lawfully admitted to the United States as a permanent resident; or (bb) has not lawfully maintained lawful permanent resident status (such status not having been abandoned, rescinded, or terminated); and (II) based on the reasonable judgment of the Secretary of Homeland Security, the Secretary of State, or a consular officer\u2014 (aa) is seeking to enter or reenter the United States to engage in birth tourism and undermine the sovereignty of the United States or its territories or outlying possessions by giving birth to a child on United States soil; or (bb) is likely to give birth to a child within 10 months of entry if such alien is admitted to, or while in the United States or its territories or outlying possessions and, as a result, obtain United States citizenship for such child based on the child\u2019s birth on United States soil; or (III) as determined by the Secretary of Homeland Security or the Attorney General\u2014 (aa) has engaged in birth tourism; or (bb) while physically present in the United States or its territories or outlying possessions, is likely to give birth to a child and, as a result, obtain United States citizenship for such child based on the child\u2019s birth on United States soil. (iii) Waiver not authorized The grounds of inadmissibility specified in this subparagraph may not be waived. (iv) Ineligibility for parole An alien who is inadmissible under this subparagraph is not be eligible for parole into the United States under section 212(d)(5) or for conditional parole under section 236. .\n##### (b) Grounds of deportability\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraph (F) as subparagraph (G); and\n**(2)**\nby inserting after subparagraph (E) the following:\n(F) Aliens undermining the sovereignty of United States through birth tourism (i) In general An alien is deportable if such alien\u2014 (I) (aa) is not lawfully admitted to the United States as a permanent resident; or (bb) has not lawfully maintaining lawful permanent resident status (such status not having been abandoned, rescinded, or terminated); and (II) has been convicted of an offense under section 274E, 274F, or 275(e) or under section 1546A of title 18, United States Code; or (III) is described in section 212(a)(2)(F). (ii) Waiver not authorized The grounds of deportability specified in clause (i) may not be waived. (iii) Ineligibility for parole An alien who is deportable under clause (i) is not be eligible for parole into the United States under section 212(d)(5) or for conditional parole under section 236. .\n#### 3. Mandatory detention for criminal aliens inadmissible or subject to deportation for birth tourism\nSection 236(c)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c)(1) ) is amended\u2014\n**(1)**\nat the end of each of subparagraphs (A), (B), and (C), by striking the comma at the end;\n**(2)**\nin subparagraph (D), by striking , or at the end and inserting a semicolon;\n**(3)**\nin subparagraph (E)(ii), by striking the comma at the end and inserting ; or ; and\n**(4)**\nby inserting after subparagraph (E)(ii) the following:\n(F) is inadmissible under section 212(a)(2)(F) or deportable under section 237(a)(2)(F) by reason of having been convicted of, admitting to having committed, or admitting committing acts that are the essential elements of, an offense under sections 274E, 274F, or 275(e), or of section 1546A of title 18, United States Code, .\n#### 4. Expedited removal for aliens engaged in birth tourism\nSection 235 of the Immigration and Nationality Act ( 8 U.S.C. 1225 ) is amended by adding at the end the following:\n(e) Removal of aliens based on birth tourism (1) Removal without further hearing An immigration officer who determines an alien is inadmissible under section 212(a)(2)(F) or deportable under section 237(a)(2)(F)\u2014 (A) shall order the alien removed, subject to review in accordance with paragraph (2); (B) shall report the order of removal to the immigration court as expeditiously as possible, but in no case later than 7 days after the date of such determination; and (C) may not conduct any further inquiry or hearing or execute the order of removal until ordered by the immigration judge pursuant to paragraph (2). (2) Review of order by immigration judge (A) In general An immigration judge shall review each administrative removal order issued pursuant to paragraph (1) not later than 7 days after such order is referred to the court by the immigration officer. (B) Removal order If an immigration judge determines that an alien referred to the immigration court is inadmissible under section 212(a)(2)(F) or deportable under 237(a)(2)(F), the immigration judge shall order the alien removed without further inquiry or hearing. (3) Burden of proof The alien shall bear the burden of proof to establish that he or she\u2014 (A) is a lawful permanent resident (such status not having been abandoned, rescinded, or terminated); or (B) is not described in section 212(a)(2)(F) or section 237(a)(4)(F). (4) Conduct of proceedings In proceedings before the immigration judge under this section, the Attorney General shall provide the alien\u2014 (A) reasonable notice of the proceeding and of the opportunity described in subparagraph (C); (B) the privilege of being represented (at no expense to the Government) by a licensed attorney at law or an accredited representative of the alien\u2019s choice who is authorized to practice before the immigration court in accordance with section 292; and (C) an opportunity to inspect the evidence and submit any additional evidence to support the alien\u2019s case prior to the review of the order by the immigration judge. (5) Treatment of aliens arriving from contiguous territory If an alien who is arriving on land (whether or not at a designated port of entry) from a foreign contiguous territory to the United States is determined by an immigration officer to be inadmissible under section 212(a)(2)(F) or deportable under section 237(a)(2)(F), the Secretary of Homeland Security shall return such alien to such territory pending a final decision under this subsection. (6) Treatment of aliens arriving in the Commonwealth of the Northern Mariana Islands or Guam If an alien who is arriving in the Commonwealth of the Northern Marianas or Guam from any foreign port of embarkation or foreign country (whether or not at a designated port of entry) is determined by an immigration officer to be inadmissible under section 212(a)(2)(F) or deportable under section 237(a)(2)(F), the Secretary of Homeland Security shall immediately return such alien to such foreign port of embarkation or foreign country pending a final decision under this subsection. (f) Prohibition on judicial review Notwithstanding section 242 of this title, any other provision of law (statutory or nonstatutory), including section 2241 of the title 28, United States Code, or any other habeas corpus provision, and sections 1361 and 1651 of such title, there shall be no judicial review of any findings (factual or legal), decisions, or actions taken by the Secretary, immigration officer, or immigration judge, pursuant to the proceedings under subsection (e). (g) Recalcitrant countries (1) Automatic suspension of visa issuance and bar to admission Notwithstanding section 243(d) or any other provision of law, if the country of birth, nationality, citizenship, or last habitual residence of an alien subject to removal under subsection (e) refuses to accept such alien within 14 days of receiving notification from the Secretary of Homeland Security of such removal order, the Secretary shall\u2014 (A) direct the Secretary of State to immediately pause the issuance of visas for all citizens, nationals, subjects, and habitual residents of such country for the following 180 days; and (B) immediately suspend admission of all citizens, nationals, subjects, and habitual residents of such country until the country accepts the return of the removed alien. (2) Exception for national security or foreign policy (A) In general The Secretary of State and the Secretary of Homeland Security may jointly determine, based on the specific circumstances of an individual alien\u2019s case, that it is in the national security or foreign policy interests of the United States to issue a visa or other travel document to an individual alien before the expiration of the 180-day period of suspension referred to in paragraph (1)(A). (B) Limitations The authority under this subsection\u2014 (i) is not subject to delegation below the Deputy Secretary of Homeland Security or the Deputy Secretary of State; (ii) may not be used to allow categories or groups of aliens of any nationality or citizenship into the United States; and (iii) may be exercised for not more than 50 aliens in any fiscal year. .\n#### 5. Mandatory medical examinations for aliens seeking visas, admission to the United States, and physically present in the United States\n##### (a) In general\nSection 221(d) of the Immigration and Nationality Act ( 8 U.S.C. 1201(d) ) is amended\u2014\n**(1)**\nby inserting after (d) the following: \u201c Physical and mental examinations .\u2014\n(1) Immigrant visas ;\n**(2)**\nin the second sentence, by striking Prior to and inserting the following:\n(2) Nonimmigrant visas (A) In general Except as provided in subparagraph (B), prior to ; and\n**(3)**\nby adding at the end the following:\n(B) Mandatory examinations (i) Medical examination Prior to the issuance of a nonimmigrant visa for business or pleasure pursuant to section 101(a)(15)(B), the Secretary of State or consular officer shall require an alien who is a biological female of childbearing age to submit to a medical examination by a medical officer of the United States Public Health Service to determine if the alien is likely to give birth in the United States or its territories or outlying possessions during the alien's stay, which will make such alien inadmissible under section 212(a)(2)(F). (ii) Medical certification A medical officer of the United States Public Health Service shall conduct the examination of an alien described in clause (i) and submit a certification to the Secretary of State or consular officer on whether the alien is likely to give birth during the alien\u2019s stay in the United States or its territories or outlying possessions. (C) Birth tourism assessment and nonimmigrant visa decisions If, based on the medical certification under subparagraph (B), the Secretary of State or consular officer suspects the alien is likely to give birth within 10 months in the United States, its territories or outlying possessions, the Secretary of State or consular officer may\u2014 (i) deny the nonimmigrant visa; or (ii) withhold visa issuance until such date as the consular officer determines the alien is no longer inadmissible under section 212(a)(2)(F)(ii). .\n##### (b) Detention for physical and mental examinations\nSection 232 of the Immigration and Nationality Act ( 8 U.S.C. 1222 ) is amended by adding at the end the following:\n(d) Detention and medical certifications for aliens subject to inadmissibility or deportability due to birth tourism (1) Detention If an immigration officer suspects an alien who is a biological female of child bearing age is inadmissible under section 212(a)(2)(F) or deportable under section 237(a)(2)(F), the Secretary of Homeland Security shall temporarily detain such alien for a sufficient period to enable a medical officer of the United States Public Health Service to determine if the alien is likely to give birth in the United States or its territories or outlying possessions during the alien\u2019s stay. (2) Medical examination and certification A medical officer of the United States Public Health Service shall conduct a physical examination, administer necessary medical tests, and certify the resulting findings for the immigration officer or immigration judge regarding whether an alien described in paragraph (1) is likely to give birth in the United States or its territories or outlying possessions during the alien\u2019s stay. .\n#### 6. Criminal penalties for facilitating birth tourism\n##### (a) In general\nChapter 8 of title II of the Immigration and Nationality Act ( 8 U.S.C. 1321 et seq. ) is amended by adding at the end the following:\n274E. Criminal penalties for facilitating birth tourism (a) Activities prohibited It shall be unlawful for any person to knowingly\u2014 (1) forge, counterfeit, alter, falsely make, or attempt to forge, counterfeit, alter, falsely make any document; (2) provide an alien any forged, counterfeit, altered, or falsely made document; or (3) prepare, file, or assist an alien with an application for a visa, travel document or other immigration benefit under this title; or (b) Criminal penalties Any individual described in subsection (a), shall be fined under title 18, United States Code, imprisoned for not less than 10 years, or both. 274F. Criminal penalties for health care matters related to birth tourism (a) Healthcare theft or embezzlement through birth tourism Any person, who knowingly\u2014 (1) embezzles, steals, or otherwise without authority converts to the use of any person other than the rightful owner; or (2) misapplies any of the moneys, funds, securities, premiums, credits, property, or other assets of a Federal health care program, to facilitate, engage in, encourage, solicit, or advertise to an alien any services related to birth tourism (regardless of whether such services, or a portion of such services, were initiated inside or outside the United States), to allow such alien to enter or remain in the United States, its territories or outlying possessions, solely to give birth to a child on United States soil in order to obtain United States citizenship for a child, shall be fined under title 18, United States Code, and imprisoned for not less than 10 years, or both. (b) Healthcare fraud through birth tourism Whoever knowingly executes, or attempts to execute, a scheme or artifice to\u2014 (1) to defraud any Federal healthcare program; or (2) to obtain, by means of false or fraudulent pretenses, representations, or promises, any of the money or property owned by, or under the custody or control of, any Federal healthcare program, in connection with the delivery of or payment for health care benefits, items, or services, for the purpose of allowing an alien to give birth to a child on United States soil in order to obtain United States citizenship for such child, shall be fined under this title or imprisoned not more than 10 years, or both. (c) Definition As used in this section, the term Federal healthcare program has the meaning given such term in section 1302a\u20137b(f) of title 42, United States Code. .\n##### (b)\nSection 275 of the Immigration and Nationality Act, 8 U.S.C. 1325 , is amended by\u2014\n**(1)**\nrevising the title of the section to read: Improper entry by alien; fraud and evasion of immigration laws .\n**(2)**\nadding a new subsection (e) to read as follows:\n(e) Birth tourism fraud Any individual who\u2014 (1) commits any act that the individual knows or reasonably should have known provides an alien with housing, transportation, food, medical care, or travel via any mode to the United States, its territories or outlying possessions; (2) commits any act that the individual knows or reasonably should have known allows an alien to receive any financial support, including expenses associated with food, medical care, housing, and transportation, that will allow the alien to enter the United States, its territories or outlying possessions, or attempt to enter the United States, its territories or outlying possessions; or (3) conspires to assist an alien to enter the United States, its territories or outlying possessions, under false pretenses, through fraud, or material misrepresentations in a visa application or other entry document, to obtain United States citizenship for the alien\u2019s child, shall be fined imprisoned for not less than 10 years and not more than 25 years, or both. .\n##### (c)\nTitle 18 of the United States Code is further amended by adding a new section 1546A to read as follows:\n1546A. Fraud, conspiracy, and other acts associated with undermining United States sovereignty through birth tourism (a) Any person who knowingly\u2014 (1) aids or assist any alien to enter the United States, its territories or outlying possessions, or to physically remain in the United States, its territories or outlying possessions, regardless of the alien\u2019s manner of entry; (2) conspires or connives, or attempts to conspire or connive to aid or assist any alien to enter the United States, its territories or outlying possessions, or to physically remain in the United States, its territories or outlying possessions; or (3) conspires or connives, or attempts to conspire or connive with any other person or persons to aid or assist any alien to enter the United States, its territories or outlying possessions, or remain in the United States, its territories or outlying possessions, for the purpose of giving birth to a child in the United States, its territories or outlying possessions, so that such child can obtain United States citizenship at birth, shall be imprisoned for a minimum of 10 years and fined $100,000 for each alien such person aided or assisted. .\n#### 7. Birth tourism taskforce\nTitle II, Chapter 9 of the Immigration and Nationality Act is amended to add a new section 295 to read as follows:\n295. Taskforce on birth tourism (a) Establishment There is established a Taskforce (hereinafter referred to as the Taskforce ) within the Department of Homeland Security, that shall include U.S. Citizenship and Immigration Services, U.S. Immigration and Customs Enforcement, Homeland Security Investigations, and U.S. Customs and Border Protection, that shall: (1) investigate individuals, organizations and entities that create schemes and run operations to facilitate in and enforce laws to prevent an alien from seeking to undermine the sovereignty of the United States by attempting to enter, entering, or remaining physically in the United States, its territories or outlying possessions, for the purpose of giving birth to a child on United States soil; and (2) refer cases to the Department of Justice for criminal prosecutions. (b) Training materials The Taskforce shall produce training materials for local law enforcement on the investigation and detection of criminal offenses described in subsection (a). (c) Coordination The Taskforce shall coordinate with the Department of Agriculture, the Office of Inspector General of the Department of Agriculture, the Federal Bureau of Investigation, the United States Marshals Service, U.S. Customs and Border Protection, and other agencies, as appropriate. (d) Report On the date that is one year after the date of enactment of this Act, and annually thereafter, the Taskforce shall submit to the appropriate committees of Congress, a report on, for the previous year\u2014 (1) the number of charges that were filed for violations of laws described in subsection (a), disaggregated by the law alleged to have been violated, the State in which the violation was alleged to have occurred, and the number of convictions; and (2) the number of investigations of violations of laws described in subsection (a) for which charges were not filed. (e) Appropriate committees defined For purposes of this section, the term appropriate committees includes\u2014 (1) the Senate Committee on the Judiciary; (2) the House Committee on the Judiciary; (3) the Senate Homeland Security and Governmental Affairs Committee; (4) the House Committee on Homeland Security; (5) the House Foreign Affairs Committee; (6) the Senate Foreign Relations Committee; and (7) the House Oversight and Government Reform Committee. .\n#### 8. Exemption from Paperwork Reduction Act and the Administrative Procedure Act\n##### (a) Paperwork Reduction Act\nNothing in this Act may be construed to require the Secretary of Homeland Security, the Secretary of Health and Human Services, the Secretary of State, or the Attorney General to comply with the requirements of chapter 35 of title 44, United States Code (commonly referred to as the Paperwork Reduction Act ), if the department head involved determines that compliance would impede the immediate implementation of this Act or the amendments made by this Act.\n##### (b) Administrative Procedure Act\nNothing in this Act may be construed to require the Secretary of Homeland Security, the Secretary of Health and Human Services, the Secretary of State, or the Attorney General to promulgate regulations under subchapter II of chapter 5 of title 5, United States Code (commonly referred to as the Administrative Procedure Act ), if the department head involved determines that compliance would impede the immediate implementation of this Act or the amendments made by this Act.\n#### 9. Effective date\nThis Act and the amendments made by this Act shall take effect on the date of enactment of this Act.",
      "versionDate": "2026-05-12",
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
        "name": "Immigration",
        "updateDate": "2026-05-28T14:48:49Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4501is.xml"
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
      "title": "BACK OFF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T03:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BACK OFF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Barring American Citizenship by Keeping Out Foreign Fraudsters",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to bar aliens from admission to the United States to give birth on United States soil or remaining in the United States to undermine the sovereignty of the United States through birth tourism.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T03:03:22Z"
    }
  ]
}
```
