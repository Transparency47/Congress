# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1837?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1837
- Title: DEFIANCE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1837
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2026-01-15T15:21:38Z
- Update date including text: 2026-01-15T15:21:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S3059-3060)
- 2026-01-13 - Floor: Message on Senate action sent to the House.
- 2026-01-13 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S143-147; text: CR S145-146)
- 2026-01-13 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-01-13 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-13 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-13 18:21:25 - Floor: Received in the House.
- 2026-01-13 18:23:38 - Floor: Held at the desk.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S3059-3060)
- 2026-01-13 - Floor: Message on Senate action sent to the House.
- 2026-01-13 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S143-147; text: CR S145-146)
- 2026-01-13 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-01-13 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-13 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-13 18:21:25 - Floor: Received in the House.
- 2026-01-13 18:23:38 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1837",
    "number": "1837",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "DEFIANCE Act of 2025",
    "type": "S",
    "updateDate": "2026-01-15T15:21:38Z",
    "updateDateIncludingText": "2026-01-15T15:21:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-01-13",
      "actionTime": "18:23:38",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-01-13",
      "actionTime": "18:21:25",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S143-147; text: CR S145-146)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S3059-3060)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
        "item": [
          {
            "date": "2026-01-13T16:03:26Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-05-21T18:24:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "SC"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-21",
      "state": "ME"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "UT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NM"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "VT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1837is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1837\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Durbin (for himself, Mr. Graham , Ms. Klobuchar , Mr. King , Mr. Lee , Mr. Heinrich , Mr. Welch , Mr. Schumer , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo improve rights to relief for individuals affected by non-consensual activities involving intimate digital forgeries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disrupt Explicit Forged Images And Non-Consensual Edits Act of 2025 or the DEFIANCE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nDigital forgeries, often called deepfakes, are synthetic images and videos that look realistic. The technology to create digital forgeries is now ubiquitous and easy to use. Hundreds of apps are available that can quickly generate digital forgeries without the need for any technical expertise.\n**(2)**\nDigital forgeries can be wholly fictitious but can also manipulate images of real people to depict sexually intimate conduct that did not occur. For example, some digital forgeries will paste the face of an individual onto the body of a real or fictitious individual who is nude or who is engaging in sexual activity. Another example is a photograph of an individual that is manipulated to digitally remove the clothing of the individual so that the person appears to be nude.\n**(3)**\nThe individuals depicted in such digital forgeries are profoundly harmed when the content is produced with intent to disclose, disclosed, or obtained without the consent of those individuals. These harms are not mitigated through labels or other information that indicates that the depiction is fake.\n**(4)**\nIt can be destabilizing to victims whenever those victims are depicted in intimate digital forgeries against their will, as the privacy of those victims is violated and the victims lose control over their likeness and identity.\n**(5)**\nVictims can feel helpless because the victims\u2014\n**(A)**\nmay not be able to determine who has created the content; and\n**(B)**\ndo not know how to prevent further disclosure of the intimate digital forgery or how to prevent more forgeries from being made.\n**(6)**\nVictims may be fearful of being in public out of concern that individuals the victims encounter have seen the digital forgeries. This leads to social rupture through the loss of the ability to trust, stigmatization, and isolation.\n**(7)**\nVictims of non-consensual, sexually intimate digital forgeries may experience depression, anxiety, and suicidal ideation. These victims may also experience the silencing effect in which the victims withdraw from online spaces and public discourse to avoid further abuse.\n**(8)**\nDigital forgeries are often used to\u2014\n**(A)**\nharass victims, interfering with their employment, education, reputation, or sense of safety; or\n**(B)**\ncommit extortion, sexual assault, domestic violence, and other crimes.\n**(9)**\nBecause of the harms caused by non-consensual, sexually intimate digital forgeries, such digital forgeries are considered to be a form of image-based sexual abuse.\n#### 3. Civil action relating to disclosure of intimate images\n##### (a) Definitions\nSection 1309 of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851 ) is amended\u2014\n**(1)**\nin the section heading, by inserting or nonconsensual activity involving digital forgeries after intimate images ; and\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2), by inserting competent, after conscious, ;\n**(B)**\nby striking paragraph (3);\n**(C)**\nby redesignating paragraph (4) as paragraph (3);\n**(D)**\nby redesignating paragraphs (5) and (6) as paragraphs (6) and (7), respectively;\n**(E)**\nby inserting after paragraph (3) the following:\n(4) Identifiable individual The term identifiable individual means an individual whose body appears in whole or in part in an intimate visual depiction or intimate digital forgery and who is identifiable by virtue of the individual\u2019s face, likeness, or other distinguishing characteristic, such as a unique birthmark or other recognizable feature, or from information displayed in connection with the intimate visual depiction or intimate digital forgery. (5) Intimate digital forgery (A) In general The term intimate digital forgery means any intimate visual depiction of an identifiable individual that\u2014 (i) falsely represents, in whole or in part\u2014 (I) the identifiable individual; or (II) the conduct or content that makes the visual depiction intimate; (ii) is created through the use of software, machine learning, artificial intelligence, or any other computer-generated or technological means, including by adapting, modifying, manipulating, or altering an authentic visual depiction; and (iii) is indistinguishable from an authentic visual depiction of the identifiable individual when viewed as a whole by a reasonable person. (B) Labels, disclosure, and context Any visual depiction described in subparagraph (A) constitutes an intimate digital forgery for purposes of this paragraph regardless of whether a label, information disclosed with the visual depiction, or the context or setting in which the visual depiction is disclosed states or implies that the visual depiction is not authentic. ; and\n**(F)**\nin paragraph (6)(A), as so redesignated\u2014\n**(i)**\nin clause (i), by striking or at the end;\n**(ii)**\nin clause (ii)\u2014\n**(I)**\nin subclause (I), by striking individual; and inserting individual; or ; and\n**(II)**\nby striking subclause (III); and\n**(iii)**\nby adding at the end the following:\n(iii) an identifiable individual engaging in sexually explicit conduct; and .\n##### (b) Civil action\nSection 1309(b) of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking subparagraph (A) and inserting the following:\n(A) In general Except as provided in paragraph (5)\u2014 (i) an identifiable individual whose intimate visual depiction is disclosed, in or affecting interstate or foreign commerce or using any means or facility of interstate or foreign commerce, without the consent of the identifiable individual, where such disclosure was made by a person who knows or recklessly disregards that the identifiable individual has not consented to such disclosure, may bring a civil action against that person in an appropriate district court of the United States for relief as set forth in paragraph (3); (ii) an identifiable individual who is the subject of an intimate digital forgery may bring a civil action in an appropriate district court of the United States for relief as set forth in paragraph (3) against any person that knowingly produced or possessed the intimate digital forgery with intent to disclose it, knowingly disclosed the intimate digital forgery, or knowingly solicited and received the intimate digital forgery, if\u2014 (I) the identifiable individual did not consent to such production or possession with intent to disclose, disclosure, or solicitation and receipt; (II) the person knew or recklessly disregarded that the identifiable individual did not consent to such production or possession with intent to disclose, disclosure, or solicitation and receipt; and (III) such production or possession with intent to disclose, disclosure, or solicitation and receipt, is in or affects interstate or foreign commerce or uses any means or facility of interstate or foreign commerce; and (iii) an identifiable individual who is the subject of an intimate digital forgery may bring a civil action in an appropriate district court of the United States for relief as set forth in paragraph (3) against any person that knowingly produced the intimate digital forgery if\u2014 (I) the identifiable individual did not consent to such production; (II) the person knew or recklessly disregarded that the identifiable individual\u2014 (aa) did not consent to such production; and (bb) was harmed, or was reasonably likely to be harmed, by the production; and (III) such production is in or affects interstate or foreign commerce or uses any means or facility of interstate or foreign commerce. ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin the subparagraph heading, by inserting identifiable before individuals ; and\n**(ii)**\nby striking an individual who is under 18 years of age, incompetent, incapacitated, or deceased, the legal guardian of the individual and inserting an identifiable individual who is under 18 years of age, incompetent, incapacitated, or deceased, the legal guardian of the identifiable individual ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby inserting identifiable before individual ;\n**(ii)**\nby striking depiction and inserting intimate visual depiction or intimate digital forgery ; and\n**(iii)**\nby striking distribution and inserting disclosure, solicitation, or possession ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby inserting identifiable before individual ;\n**(ii)**\nby inserting or intimate digital forgery after depiction each place it appears; and\n**(iii)**\nby inserting , solicitation, or possession after disclosure ;\n**(3)**\nby redesignating paragraph (4) as paragraph (5);\n**(4)**\nby striking paragraph (3) and inserting the following:\n(3) Relief (A) In general In a civil action filed under this section, an identifiable individual may recover\u2014 (i) damages as provided under subparagraph (C); and (ii) the cost of the action, including reasonable attorney fees and other litigation costs reasonably incurred. (B) Punitive damages and other relief The court may, in addition to any other relief available at law, award punitive damages or order equitable relief, including a temporary restraining order, a preliminary injunction, or a permanent injunction ordering the defendant to delete, destroy, or cease to display or disclose the intimate visual depiction or intimate digital forgery. (C) Damages For purposes of subparagraph (A)(i), the identifiable individual may recover\u2014 (i) liquidated damages in the amount of\u2014 (I) $150,000; or (II) $250,000 if the conduct at issue in the claim was\u2014 (aa) committed in relation to actual or attempted sexual assault, stalking, or harassment of the identifiable individual by the defendant; or (bb) the direct and proximate cause of actual or attempted sexual assault, stalking, or harassment of the identifiable individual by any person; or (ii) actual damages sustained by the individual, which shall include any profits of the defendant that are attributable to the conduct at issue in the claim that are not otherwise taken into account in computing the actual damages. (D) Calculation of defendant\u2019s profit For purposes of subparagraph (C)(ii), to establish the defendant\u2019s profits, the identifiable individual shall be required to present proof only of the gross revenue of the defendant, and the defendant shall be required to prove the deductible expenses of the defendant and the elements of profit attributable to factors other than the conduct at issue in the claim. (4) Preservation of privacy In a civil action filed under this section, the court may issue an order to protect the privacy of a plaintiff, including by\u2014 (A) permitting the plaintiff to use a pseudonym; (B) requiring the parties to redact the personal identifying information of the plaintiff from any public filing, or to file such documents under seal; and (C) issuing a protective order for purposes of discovery, which may include an order indicating that any intimate visual depiction or intimate digital forgery shall remain in the care, custody, and control of the court. ;\n**(5)**\nin paragraph (5)(A), as so redesignated\u2014\n**(A)**\nby striking image and inserting visual depiction or intimate digital forgery ; and\n**(B)**\nby striking depicted and inserting identifiable ; and\n**(6)**\nby adding at the end the following:\n(6) Statute of limitations Any action commenced under this section shall be barred unless the complaint is filed not later than 10 years from the later of\u2014 (A) the date on which the identifiable individual reasonably discovers the violation that forms the basis for the claim; or (B) the date on which the identifiable individual reaches 18 years of age. (7) Duplicative recovery barred No relief may be ordered under paragraph (3) against a person who is subject to a judgment under section 2255 of title 18, United States Code, for the same conduct involving the same identifiable individual and the same intimate visual depiction or intimate digital forgery. .\n##### (c) Continued applicability of Federal, State, and Tribal law\n**(1) In general**\nThis Act shall not be construed to impair, supersede, or limit a provision of Federal, State, or Tribal law.\n**(2) No preemption**\nNothing in this Act shall prohibit a State or Tribal government from adopting and enforcing a provision of law governing disclosure of intimate images or nonconsensual activity involving an intimate digital forgery, as defined in section 1309(a) of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851(a) ), as amended by this Act, that is at least as protective of the rights of a victim as this Act.\n#### 4. Severability; rule of construction\n##### (a) Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any person or circumstance, is held to be unconstitutional, the remaining provisions of and amendments made by this Act, and the application of the provision or amendment held to be unconstitutional to any other person or circumstance, shall not be affected thereby.\n##### (b) Rule of construction\nNothing in this Act, or an amendment made by this Act, shall be construed to limit or expand any law pertaining to intellectual property.",
      "versionDate": "2025-05-21",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1837es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 1837\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo improve rights to relief for individuals affected by non-consensual activities involving intimate digital forgeries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disrupt Explicit Forged Images And Non-Consensual Edits Act of 2025 or the DEFIANCE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nDigital forgeries, often called deepfakes, are synthetic images and videos that look realistic. The technology to create digital forgeries is now ubiquitous and easy to use. Hundreds of apps are available that can quickly generate digital forgeries without the need for any technical expertise.\n**(2)**\nDigital forgeries can be wholly fictitious but can also manipulate images of real people to depict sexually intimate conduct that did not occur. For example, some digital forgeries will paste the face of an individual onto the body of a real or fictitious individual who is nude or who is engaging in sexual activity. Another example is a photograph of an individual that is manipulated to digitally remove the clothing of the individual so that the person appears to be nude.\n**(3)**\nThe individuals depicted in such digital forgeries are profoundly harmed when the content is produced with intent to disclose, disclosed, or obtained without the consent of those individuals. These harms are not mitigated through labels or other information that indicates that the depiction is fake.\n**(4)**\nIt can be destabilizing to victims whenever those victims are depicted in intimate digital forgeries against their will, as the privacy of those victims is violated and the victims lose control over their likeness and identity.\n**(5)**\nVictims can feel helpless because the victims\u2014\n**(A)**\nmay not be able to determine who has created the content; and\n**(B)**\ndo not know how to prevent further disclosure of the intimate digital forgery or how to prevent more forgeries from being made.\n**(6)**\nVictims may be fearful of being in public out of concern that individuals the victims encounter have seen the digital forgeries. This leads to social rupture through the loss of the ability to trust, stigmatization, and isolation.\n**(7)**\nVictims of non-consensual, sexually intimate digital forgeries may experience depression, anxiety, and suicidal ideation. These victims may also experience the silencing effect in which the victims withdraw from online spaces and public discourse to avoid further abuse.\n**(8)**\nDigital forgeries are often used to\u2014\n**(A)**\nharass victims, interfering with their employment, education, reputation, or sense of safety; or\n**(B)**\ncommit extortion, sexual assault, domestic violence, and other crimes.\n**(9)**\nBecause of the harms caused by non-consensual, sexually intimate digital forgeries, such digital forgeries are considered to be a form of image-based sexual abuse.\n#### 3. Civil action relating to disclosure of intimate images\n##### (a) Definitions\nSection 1309 of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851 ) is amended\u2014\n**(1)**\nin the section heading, by inserting or nonconsensual activity involving digital forgeries after intimate images ; and\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2), by inserting competent, after conscious, ;\n**(B)**\nby striking paragraph (3);\n**(C)**\nby redesignating paragraph (4) as paragraph (3);\n**(D)**\nby redesignating paragraphs (5) and (6) as paragraphs (6) and (7), respectively;\n**(E)**\nby inserting after paragraph (3) the following:\n(4) Identifiable individual The term identifiable individual means an individual whose body appears in whole or in part in an intimate visual depiction or intimate digital forgery and who is identifiable by virtue of the individual\u2019s face, likeness, or other distinguishing characteristic, such as a unique birthmark or other recognizable feature, or from information displayed in connection with the intimate visual depiction or intimate digital forgery. (5) Intimate digital forgery (A) In general The term intimate digital forgery means any intimate visual depiction of an identifiable individual that\u2014 (i) falsely represents, in whole or in part\u2014 (I) the identifiable individual; or (II) the conduct or content that makes the visual depiction intimate; (ii) is created through the use of software, machine learning, artificial intelligence, or any other computer-generated or technological means, including by adapting, modifying, manipulating, or altering an authentic visual depiction; and (iii) is indistinguishable from an authentic visual depiction of the identifiable individual when viewed as a whole by a reasonable person. (B) Labels, disclosure, and context Any visual depiction described in subparagraph (A) constitutes an intimate digital forgery for purposes of this paragraph regardless of whether a label, information disclosed with the visual depiction, or the context or setting in which the visual depiction is disclosed states or implies that the visual depiction is not authentic. ; and\n**(F)**\nin paragraph (6)(A), as so redesignated\u2014\n**(i)**\nin clause (i), by striking or at the end;\n**(ii)**\nin clause (ii)\u2014\n**(I)**\nin subclause (I), by striking individual; and inserting individual; or ; and\n**(II)**\nby striking subclause (III); and\n**(iii)**\nby adding at the end the following:\n(iii) an identifiable individual engaging in sexually explicit conduct; and .\n##### (b) Civil action\nSection 1309(b) of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking subparagraph (A) and inserting the following:\n(A) In general Except as provided in paragraph (5)\u2014 (i) an identifiable individual whose intimate visual depiction is disclosed, in or affecting interstate or foreign commerce or using any means or facility of interstate or foreign commerce, without the consent of the identifiable individual, where such disclosure was made by a person who knows or recklessly disregards that the identifiable individual has not consented to such disclosure, may bring a civil action against that person in an appropriate district court of the United States for relief as set forth in paragraph (3); (ii) an identifiable individual who is the subject of an intimate digital forgery may bring a civil action in an appropriate district court of the United States for relief as set forth in paragraph (3) against any person that knowingly produced or possessed the intimate digital forgery with intent to disclose it, knowingly disclosed the intimate digital forgery, or knowingly solicited and received the intimate digital forgery, if\u2014 (I) the identifiable individual did not consent to such production or possession with intent to disclose, disclosure, or solicitation and receipt; (II) the person knew or recklessly disregarded that the identifiable individual did not consent to such production or possession with intent to disclose, disclosure, or solicitation and receipt; and (III) such production or possession with intent to disclose, disclosure, or solicitation and receipt, is in or affects interstate or foreign commerce or uses any means or facility of interstate or foreign commerce; and (iii) an identifiable individual who is the subject of an intimate digital forgery may bring a civil action in an appropriate district court of the United States for relief as set forth in paragraph (3) against any person that knowingly produced the intimate digital forgery if\u2014 (I) the identifiable individual did not consent to such production; (II) the person knew or recklessly disregarded that the identifiable individual\u2014 (aa) did not consent to such production; and (bb) was harmed, or was reasonably likely to be harmed, by the production; and (III) such production is in or affects interstate or foreign commerce or uses any means or facility of interstate or foreign commerce. ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin the subparagraph heading, by inserting identifiable before individuals ; and\n**(ii)**\nby striking an individual who is under 18 years of age, incompetent, incapacitated, or deceased, the legal guardian of the individual and inserting an identifiable individual who is under 18 years of age, incompetent, incapacitated, or deceased, the legal guardian of the identifiable individual ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby inserting identifiable before individual ;\n**(ii)**\nby striking depiction and inserting intimate visual depiction or intimate digital forgery ; and\n**(iii)**\nby striking distribution and inserting disclosure, solicitation, or possession ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby inserting identifiable before individual ;\n**(ii)**\nby inserting or intimate digital forgery after depiction each place it appears; and\n**(iii)**\nby inserting , solicitation, or possession after disclosure ;\n**(3)**\nby redesignating paragraph (4) as paragraph (5);\n**(4)**\nby striking paragraph (3) and inserting the following:\n(3) Relief (A) In general In a civil action filed under this section, an identifiable individual may recover\u2014 (i) damages as provided under subparagraph (C); and (ii) the cost of the action, including reasonable attorney fees and other litigation costs reasonably incurred. (B) Punitive damages and other relief The court may, in addition to any other relief available at law, award punitive damages or order equitable relief, including a temporary restraining order, a preliminary injunction, or a permanent injunction ordering the defendant to delete, destroy, or cease to display or disclose the intimate visual depiction or intimate digital forgery. (C) Damages For purposes of subparagraph (A)(i), the identifiable individual may recover\u2014 (i) liquidated damages in the amount of\u2014 (I) $150,000; or (II) $250,000 if the conduct at issue in the claim was\u2014 (aa) committed in relation to actual or attempted sexual assault, stalking, or harassment of the identifiable individual by the defendant; or (bb) the direct and proximate cause of actual or attempted sexual assault, stalking, or harassment of the identifiable individual by any person; or (ii) actual damages sustained by the individual, which shall include any profits of the defendant that are attributable to the conduct at issue in the claim that are not otherwise taken into account in computing the actual damages. (D) Calculation of defendant\u2019s profit For purposes of subparagraph (C)(ii), to establish the defendant\u2019s profits, the identifiable individual shall be required to present proof only of the gross revenue of the defendant, and the defendant shall be required to prove the deductible expenses of the defendant and the elements of profit attributable to factors other than the conduct at issue in the claim. (4) Preservation of privacy In a civil action filed under this section, the court may issue an order to protect the privacy of a plaintiff, including by\u2014 (A) permitting the plaintiff to use a pseudonym; (B) requiring the parties to redact the personal identifying information of the plaintiff from any public filing, or to file such documents under seal; and (C) issuing a protective order for purposes of discovery, which may include an order indicating that any intimate visual depiction or intimate digital forgery shall remain in the care, custody, and control of the court. ;\n**(5)**\nin paragraph (5)(A), as so redesignated\u2014\n**(A)**\nby striking image and inserting visual depiction or intimate digital forgery ; and\n**(B)**\nby striking depicted and inserting identifiable ; and\n**(6)**\nby adding at the end the following:\n(6) Statute of limitations Any action commenced under this section shall be barred unless the complaint is filed not later than 10 years from the later of\u2014 (A) the date on which the identifiable individual reasonably discovers the violation that forms the basis for the claim; or (B) the date on which the identifiable individual reaches 18 years of age. (7) Duplicative recovery barred No relief may be ordered under paragraph (3) against a person who is subject to a judgment under section 2255 of title 18, United States Code, for the same conduct involving the same identifiable individual and the same intimate visual depiction or intimate digital forgery. .\n##### (c) Continued applicability of Federal, State, and Tribal law\n**(1) In general**\nThis Act shall not be construed to impair, supersede, or limit a provision of Federal, State, or Tribal law.\n**(2) No preemption**\nNothing in this Act shall prohibit a State or Tribal government from adopting and enforcing a provision of law governing disclosure of intimate images or nonconsensual activity involving an intimate digital forgery, as defined in section 1309(a) of the Consolidated Appropriations Act, 2022 ( 15 U.S.C. 6851(a) ), as amended by this Act, that is at least as protective of the rights of a victim as this Act.\n#### 4. Severability; rule of construction\n##### (a) Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any person or circumstance, is held to be unconstitutional, the remaining provisions of and amendments made by this Act, and the application of the provision or amendment held to be unconstitutional to any other person or circumstance, shall not be affected thereby.\n##### (b) Rule of construction\nNothing in this Act, or an amendment made by this Act, shall be construed to limit or expand any law pertaining to intellectual property.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-05-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3562",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DEFIANCE Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-01-14T15:25:47Z"
          },
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Photography and imaging",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-01-14T15:27:49Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2026-01-14T15:27:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-18T14:08:43Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1837is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1837es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "DEFIANCE Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-01-14T14:09:55Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Disrupt Explicit Forged Images And Non-Consensual Edits Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-01-14T14:09:55Z"
    },
    {
      "title": "DEFIANCE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T12:03:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DEFIANCE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disrupt Explicit Forged Images And Non-Consensual Edits Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve rights to relief for individuals affected by non-consensual activities involving intimate digital forgeries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T04:18:24Z"
    }
  ]
}
```
