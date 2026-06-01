# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8341?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8341
- Title: DEPORT Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8341
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-30T18:30:28Z
- Update date including text: 2026-04-30T18:30:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8341",
    "number": "8341",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001235",
        "district": "2",
        "firstName": "Riley",
        "fullName": "Rep. Moore, Riley M. [R-WV-2]",
        "lastName": "Moore",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "DEPORT Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-30T18:30:28Z",
    "updateDateIncludingText": "2026-04-30T18:30:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:05:00Z",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "AL"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "AZ"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "GA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "MO"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OK"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "FL"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "GA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8341ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8341\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Moore of West Virginia (for himself, Mr. Gill of Texas , Mr. Fine , Mr. Hunt , Ms. Mace , Mr. Ogles , Mr. Moore of Alabama , Mr. Crane , and Mr. Carter of Georgia ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to require an attestation disavowing terrorist intent prior to naturalization of any alien.\n#### 1. Short title\nThis Act may be cited as the Denaturalization and Expulsion of Persons who Orchestrate Radical Terrorism Act of 2026 or as the DEPORT Act of 2026 .\n#### 2. Terrorism attestation requirement for naturalization\nSection 316 of the Immigration and Nationality Act ( 8 U.S.C. 1427 ) is amended by adding at the end the following:\n(g) Terrorism attestation (1) In general As a condition of naturalization, each applicant shall execute under oath and under penalty of perjury a written attestation, on such form as the Secretary of Homeland Security shall prescribe, that the applicant\u2014 (A) has not been convicted of, or had charges pending for, any covered offense, as defined in paragraph (4), at the time of the naturalization application or oath of allegiance; and (B) does not, at the time of naturalization, possess an intent to commit any covered offense in the future. (2) Form requirement Not later than 180 days after the date of enactment of this subsection, the Secretary of Homeland Security shall revise the application for naturalization (Form N\u2013400, or any successor form) to include the attestation required under paragraph (1), with each covered offense listed individually, requiring the applicant to separately affirm compliance as to each such offense. (3) Oath requirement The oath of allegiance administered under section 337 shall include an express renunciation of any intent to engage in any covered offense against the United States or its people. (4) Covered offenses defined For purposes of this subsection and section 340(f), the term covered offense means any of the following: (A) Any Federal crime of terrorism, as defined in section 2332b(g)(5) of title 18, United States Code. (B) Any offense under section 2339A of title 18, United States Code (relating to providing material support to terrorists). (C) Any offense under section 2339B of title 18, United States Code (relating to providing material support or resources to designated foreign terrorist organizations). (D) Any offense under section 2339C of title 18, United States Code (relating to financing of terrorism). (E) Any offense under section 2339D of title 18, United States Code (relating to receiving military-type training from a foreign terrorist organization). (F) Any offense under section 2332a of title 18, United States Code (relating to use of weapons of mass destruction). (G) Any offense under sections 175, 175c, or 178 of title 18, United States Code (relating to biological weapons). (H) Any offense under section 229 of title 18, United States Code (relating to chemical weapons). (I) Any offense under section 831 of title 18, United States Code (relating to prohibited transactions involving nuclear materials). (J) Any offense under section 32 of title 18, United States Code (relating to destruction of aircraft or aircraft facilities). (K) Any offense under section 37 of title 18, United States Code (relating to violence at international airports). (L) Any offense under section 1203 of title 18, United States Code (relating to hostage taking). (M) Any offense under section 2280 or 2281 of title 18, United States Code (relating to violence against maritime navigation or maritime fixed platforms). (N) Any offense under section 2332 of title 18, United States Code (relating to criminal penalties involving the killing of United States nationals abroad). (O) Any offense under section 2332b of title 18, United States Code (relating to acts of terrorism transcending national boundaries). (P) Any offense under section 2332f of title 18, United States Code (relating to bombings of places of public use, government facilities, public transportation systems, and infrastructure facilities). (Q) Any offense under section 2332g or 2332h of title 18, United States Code (relating to missile systems designed to destroy aircraft and radiological dispersal devices). (R) Any offense under section 2332i of title 18, United States Code (relating to acts of nuclear terrorism). (S) Any offense under section 2384 of title 18, United States Code (relating to seditious conspiracy). (T) Any offense under section 1992 of title 18, United States Code (relating to terrorist attacks and other violence against railroad carriers and against mass transportation systems on land, on water, or through the air). (U) Any offense under section 2283 or 2284 of title 18, United States Code (relating to transportation of explosives, destructive devices, and biological, chemical, nuclear, or radiological weapons, or transportation of terrorists). (V) Any conspiracy to commit, or attempt to commit, any of the offenses described in subparagraphs (A) through (U). .\n#### 3. Terrorism convictions and conduct as evidence of illegal procurement of naturalization\nSection 340 of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following: A conviction, finding, admission, or other credible evidence described in subsection (f) may constitute evidence that naturalization was illegally procured or procured by concealment of a material fact or by willful misrepresentation. ; and\n**(2)**\nby adding at the end the following:\n(i) Terrorism-Related conduct as evidence of illegal procurement (1) Prima facie evidence of ineligibility for prior naturalization For any person who was naturalized prior to the effective date of the attestation requirement under section 316(g), a conviction described in paragraph (2), or a judicial or administrative finding, admission by the person, or other credible evidence of conduct described in paragraph (2), occurring within 10 years after the date of naturalization, shall constitute prima facie evidence that\u2014 (A) the person lacked good moral character under section 101(f), attachment to the principles of the Constitution of the United States under section 316(a), and disposition to the good order and happiness of the United States required for naturalization; and (B) the order admitting the person to citizenship and the certificate of naturalization were illegally procured or procured by concealment of a material fact or by willful misrepresentation. The 10-year period in this paragraph shall apply unless judicially determined to be unconstitutional as applied, in which case a 7-year period shall apply, and if that period is likewise determined unconstitutional, a 5-year period shall apply. (2) Covered offenses and conduct The convictions, findings, admissions, or evidence described in this paragraph are\u2014 (A) a conviction by a final judgment, after exhaustion of direct appeals, in any Federal court of competent jurisdiction, or by court-martial under chapter 47 of title 10, United States Code, for any covered offense as defined in section 316(g)(4), including any attempt or conspiracy to commit such an offense; (B) knowing membership in, or material support to, a foreign terrorist organization designated under section 219 of this Act, or any organization engaged in terrorist activity as defined in section 212(a)(3)(B), where the person\u2014 (i) knew or reasonably should have known of the organization\u2019s designation or terrorist character at the time of membership or support; (ii) actively participated in or materially contributed to the organization\u2019s activities, finances, recruitment, or operations; and (iii) did not take affirmative steps to disassociate upon learning of the organization\u2019s terrorist character; or (C) clear and convincing evidence, established through judicial findings in a civil proceeding under paragraph (4), that the person engaged in specific overt acts constituting terrorist activity as defined in section 212(a)(3)(B), where such evidence includes corroborating documentation, witness testimony, or other independently verifiable proof, and where the person has been afforded full opportunity to contest such evidence. (3) Presumption of illegal procurement based on attestation For any naturalized citizen who executed an attestation under section 316(g), a subsequent conviction for a covered offense as defined in section 316(g)(4), regardless of when such conviction occurs, shall constitute evidence that naturalization was procured by concealment of a material fact or by willful misrepresentation. Specifically\u2014 (A) for conduct occurring, in whole or in part, prior to the date of naturalization, such conviction shall create a rebuttable presumption that the attestation required under section 316(g)(1)(A) was false at the time it was made; and (B) for conduct occurring entirely after the date of naturalization, such conviction shall create a rebuttable presumption that the person did not possess a genuine intent to refrain from committing a covered offense at the time the attestation under section 316(g)(1)(B) was executed. The presumption in either case may be rebutted only by the defendant establishing, by clear, convincing, and unequivocal evidence, that the attestation was truthful at the time it was made and that they possessed a genuine intent to comply with the attestation at the time of naturalization. Where the defendant produces evidence sufficient to rebut the presumption, the burden of persuasion on the ultimate question of illegal procurement shall return to the Government, which must then establish such procurement by clear, convincing, and unequivocal evidence. (4) Procedures (A) Proceedings under this subsection shall be brought by the Attorney General, acting through the Department of Justice, in a civil action filed in the United States district court for the district in which the person resides or is found. (B) Except where a presumption is established under paragraph (3), the Government shall bear the burden of establishing the grounds for revocation by clear, convincing, and unequivocal evidence. (C) Revocation of naturalization under this subsection shall take effect on the date of the final order of the court revoking naturalization. (D) Upon entry of a final order revoking naturalization under this subsection, the Secretary of Homeland Security shall initiate removal proceedings pursuant to section 240 of this Act. The United States attorney for the district in which a covered conviction is obtained shall notify the Secretary of Homeland Security not later than 30 days after the date on which such conviction becomes final. (E) The Attorney General may initiate proceedings under this subsection based on evidence of conduct described in paragraph (2)(C) absent a final criminal conviction only where\u2014 (i) a federal grand jury has returned an indictment for conduct described in paragraph (2)(A), or a federal court has made a judicial finding of probable cause for such conduct; (ii) the person has been provided notice and a meaningful opportunity to be heard before a neutral adjudicator; (iii) the Government establishes its case by clear, convincing, and unequivocal evidence; (iv) the civil proceeding is stayed if criminal proceedings on the same conduct are pending, unless the person consents to simultaneous proceedings; and (v) where the evidence supporting the proceedings includes classified information, the Attorney General, in consultation with the Director of National Intelligence, may file a classified certification with the reviewing court attesting that\u2014 (I) the classified information has been reviewed by the court in camera and ex parte; (II) disclosure of such information would cause identifiable harm to national security; and (III) the classified information, considered together with any unclassified evidence, establishes the evidentiary standard required under subparagraph (B); provided that the person is afforded a meaningful opportunity to contest the unclassified portions of the government\u2019s case and to submit rebuttal evidence. (5) Statelessness and removal authority (A) If revocation of naturalization under this subsection would render the person stateless and removal cannot be effectuated, the person shall be detained in accordance with section 241 of this Act ( 8 U.S.C. 1231 ) until removal becomes practicable. (B) Notwithstanding subparagraph (A), where revocation is based on terrorism-related conduct under this subsection, the Attorney General may seek continued detention beyond the presumptive removal period by filing a certification with the reviewing district court that\u2014 (i) removal to any available country is actively being pursued; (ii) the person has been individually assessed and determined to pose a specific, articulable threat to national security or public safety; and (iii) detention is reviewed by the court no less frequently than every 180 days. Such certification shall not authorize permanent indefinite detention absent continued judicial authorization. (6) Applicability to prior naturalizations With respect to any person naturalized prior to the effective date of the attestation requirement under section 316(g), a conviction for a covered offense shall constitute independent grounds for the institution of denaturalization proceedings under section 340(a), on the basis that such conviction constitutes evidence that naturalization was procured by concealment of a material fact, to the extent that the person failed to disclose prior convictions, pending charges, or intent to engage in conduct constituting a covered offense at the time of the naturalization application or oath of allegiance. (7) No time limitation There shall be no statute of limitations for proceedings under this subsection. .\n#### 4. Deportability of denaturalized persons\nSection 237(a) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a) ) is amended by adding at the end the following:\n(9) Aliens denaturalized under section 340 Any alien whose naturalization has been revoked pursuant to section 340 shall be deportable and subject to removal proceedings under this title. .\n#### 5. Inadmissibility for covered terrorism convictions\nSection 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2) ) is amended by adding at the end the following:\n(K) Federal terrorism convictions Any alien who has been convicted of a covered offense, as that term is defined in section 316(g)(4) of this Act, is inadmissible. .\n#### 6. Revocation of immigration benefits and status\n##### (a) In general\nSubject to judicial review, any alien who has been convicted of a covered offense, as that term is defined in section 316(g)(4) of the Immigration and Nationality Act, shall be\u2014\n**(1)**\nrendered ineligible for any immigration benefit under the immigration laws, including\u2014\n**(A)**\nadjustment of status under section 245 of such Act;\n**(B)**\nany form of relief from removal, including cancellation of removal, voluntary departure, and asylum;\n**(C)**\nany classification as a nonimmigrant under section 101(a)(15) of such Act;\n**(D)**\ntemporary protected status under section 244 of such Act;\n**(E)**\ndeferred action, parole, or any other discretionary grant of permission to remain in the United States; and\n**(F)**\nnaturalization under title III of such Act;\n**(2)**\nsubject to removal proceedings under section 240 of the Immigration and Nationality Act; and\n**(3)**\nsubject to detention during such proceedings pursuant to section 236(c) of such Act, subject to judicial review as provided under existing law.\n##### (b) Revocation of existing benefits\nAny immigration benefit or status previously granted to an alien described in subsection (a), including lawful permanent resident status, any nonimmigrant status, temporary protected status, deferred action, or parole, shall be revoked upon entry of a final order of removal or denaturalization, subject to judicial review.\n##### (c) No waiver\nNo waiver under any provision of the Immigration and Nationality Act shall be available with respect to any ground of inadmissibility or deportability arising under this section or section 5 of this Act.\n#### 7. Permanent bar to admission\nSection 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2) ) (as amended by this Act) is further amended by adding at the end the following:\n(L) Permanent bar for certain terrorist offenders Any person whose naturalization is revoked under section 340 or who has previously been ordered removed for conviction for a covered offense, as that term is defined in section 316(g)(4) of this Act, is inadmissible (including any person inadmissible under subparagraph (K)). No waiver of inadmissibility under any provision of this Act or any other provision of law shall be available to such alien. .\n#### 8. Conforming amendment\nSection 340(f) of the Immigration and Nationality Act ( 8 U.S.C. 1451(f) ) is amended by adding at the end the following: On entry of a final order of revocation under this subsection, the court shall revoke and set aside the citizenship order and cancel the certificate of naturalization. .\n#### 9. Rule of construction\nNothing in this Act shall be construed to\u2014\n**(1)**\ncreate any new basis for denaturalization other than through the existing authority under section 340(a) of the Immigration and Nationality Act, as supplemented by the presumptions established in section 340(f) of such Act, as added by this Act;\n**(2)**\nlimit the authority of the United States to institute proceedings under section 340(a) of such Act on any other basis, including illegal procurement, concealment of a material fact, or willful misrepresentation unrelated to the attestation required under section 316(g) of such Act;\n**(3)**\nlimit the authority of the Department of Homeland Security or the Department of Justice to bring any criminal or civil action under any other provision of law; or\n**(4)**\nauthorize the denaturalization of any person who is a citizen of the United States by birth.\n#### 10. Severability\nIf any provision of this Act, or the application of any provision to any person or circumstance, is held invalid, the remainder of this Act and the application of its provisions shall not be affected.\n#### 11. Effective date\n##### (a) In general\nThis Act and the amendments made by this Act shall take effect on the date of enactment of this Act.\n##### (b) Attestation requirement\nThe attestation requirement under section 316(g) of the Immigration and Nationality Act, as added by section 2 of this Act, shall apply to all applications for naturalization filed on or after the date that is 180 days after the date of enactment of this Act.\n##### (c) Inadmissibility, deportability, and benefit revocation\nThe amendments made by sections 5 and 6 of this Act shall apply to any conviction entered on or after the date of enactment of this Act, regardless of when the underlying conduct occurred.",
      "versionDate": "2026-04-16",
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
        "updateDate": "2026-04-30T18:30:27Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8341ih.xml"
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
      "title": "DEPORT Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DEPORT Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Denaturalization and Expulsion of Persons who Orchestrate Radical Terrorism Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to require an attestation disavowing terrorist intent prior to naturalization of any alien.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:34Z"
    }
  ]
}
```
