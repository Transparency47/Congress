# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/353?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/353
- Title: Impeaching Donald John Trump, President of the United States, for high crimes and misdemeanors.
- Congress: 119
- Bill type: HRES
- Bill number: 353
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2025-05-16T15:52:07Z
- Update date including text: 2025-05-16T15:52:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-04-28 - IntroReferral: Submitted in House
- 2025-04-28 - IntroReferral: Submitted in House
- 2025-05-13 - IntroReferral: Sponsor introductory remarks on measure. (CR H1953)
- 2025-05-13 14:16:00 - Floor: NOTIFICATION OF INTENT TO OFFER RESOLUTION - Mr. Thanedar notified the House of his intent to offer a privileged resolution pursuant to clause 2(a)(1) of rule IX. The Chair announced that a determination will be made at the time designated for consideration of the resolution.
- Latest action: 2025-04-28: Submitted in House

## Actions

- 2025-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-04-28 - IntroReferral: Submitted in House
- 2025-04-28 - IntroReferral: Submitted in House
- 2025-05-13 - IntroReferral: Sponsor introductory remarks on measure. (CR H1953)
- 2025-05-13 14:16:00 - Floor: NOTIFICATION OF INTENT TO OFFER RESOLUTION - Mr. Thanedar notified the House of his intent to offer a privileged resolution pursuant to clause 2(a)(1) of rule IX. The Chair announced that a determination will be made at the time designated for consideration of the resolution.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/353",
    "number": "353",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000488",
        "district": "13",
        "firstName": "Shri",
        "fullName": "Rep. Thanedar, Shri [D-MI-13]",
        "lastName": "Thanedar",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Impeaching Donald John Trump, President of the United States, for high crimes and misdemeanors.",
    "type": "HRES",
    "updateDate": "2025-05-16T15:52:07Z",
    "updateDateIncludingText": "2025-05-16T15:52:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2025-05-13",
      "actionTime": "14:16:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "NOTIFICATION OF INTENT TO OFFER RESOLUTION - Mr. Thanedar notified the House of his intent to offer a privileged resolution pursuant to clause 2(a)(1) of rule IX. The Chair announced that a determination will be made at the time designated for consideration of the resolution.",
      "type": "Floor"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1953)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
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
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-04-28T16:01:30Z",
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
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "sponsorshipWithdrawnDate": "2025-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "sponsorshipWithdrawnDate": "2025-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "sponsorshipWithdrawnDate": "2025-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "sponsorshipWithdrawnDate": "2025-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres353ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 353\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Mr. Thanedar (for himself, Mr. Mfume , Mr. Nadler , and Ms. Kelly of Illinois ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nImpeaching Donald John Trump, President of the United States, for high crimes and misdemeanors.\nThat Donald John Trump, President of the United States, is impeached for high crimes and misdemeanors, and that the following articles of impeachment be exhibited to the Senate:\nArticle of impeachment exhibited by the House of Representatives of the United States of America in the name of itself and of the people of the United States of America, against Donald John Trump, President of the United States of America, in maintenance and support of its impeachment against him for high crimes and misdemeanors.\n#### Article I: Obstruction of Justice, Violation of Due Process, and a Breach of the Duty to Faithfully Execute Laws\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that the President shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors . Further, Article II of the Constitution states that the President shall take Care that the Laws be faithfully executed , the Fourth Amendment of the Constitution states that The right of the people \u2026 against unreasonable searches and seizures, shall not be violated , and the Fifth Amendment of the Constitution states No person shall be \u2026 deprived of life, liberty, or property, without due process of law . In his conduct of the office of President of the United States\u2014and in violation of his constitutional oath to faithfully to execute the office of President of the United States and, to the best of his ability, preserve, protect, and defend the Constitution of the United States, and in violation of his constitutional duty to take care that the laws be faithfully executed\u2014Donald John Trump has abused the powers of the Presidency in a manner offensive to, and subversive of, the Constitution, in that:\nUsing the power of his high office, Donald John Trump has engaged in this scheme or course of conduct through the following means:\n**(1)**\nBy his orders and directions to subordinates, obstructed the administration of justice and embarked on a scheme to destroy and corrupt the legal system and the powers of the courts under Article III of the Constitution. Specifically, he has done the following:\n**(A)**\nDirected and permitted his subordinates and attorneys at the Department of Justice to violate their oaths to uphold the Constitution, laws of the United States, and the rules of professional ethics by adducing misleading and willfully false representations to the courts of the United States, and to otherwise abuse their official powers. Specifically, he has\u2014\n**(i)**\nsought to dismiss, without prejudice and under false pretenses, the bribery and fraud charges against New York City Mayor Eric Adams, in an unethical quid pro quo exchange for the Defendant\u2019s cooperation with the Administration\u2019s political priorities, thus abusing the criminal laws to unconstitutionally commandeer a State officer and unit of government in violation of the sovereignty thereof; and\n**(ii)**\nterminated and purged career Department of Justice attorneys without reasonable cause and in violation of the law in retaliation for their legitimate investigatory and prosecutorial work under prior administrations, including in relation to the January 6, 2021, attack on the United States Capitol, and in retaliation for attorneys upholding their ethical and legal obligations including candor and honesty to the courts.\n**(B)**\nDirected and permitted the evasion and defiance of binding court orders. Specifically, he has\u2014\n**(i)**\nremoved persons from the United States to El Salvador despite an order from the United States District Court for the District of Columbia, for which said Court has found probable cause that the Government committed acts of criminal contempt;\n**(ii)**\nremoved Kilmar Armando Abrego Garcia from the United States to El Salvador despite a binding Withholding of Removal order prohibiting the government from removing him to El Salvador;\n**(iii)**\ndefied court orders, upheld by a unanimous ruling of the Supreme Court, to facilitate the release of Mr. Abrego Garcia, and related orders to provide information to the court and opposing counsel, while publicly flaunting their refusal;\n**(iv)**\nacted in contempt of court for violating a court-sanctioned settlement agreement; and\n**(v)**\nconducted enforced disappearances of persons without due process and without disclosing their fate and location to their families and legal counsel, in violation of the Constitution and the rulings of the Supreme Court, as well as the foundational principles of due process and the rule of law.\n**(C)**\nDirected and permitted the deliberate and systematic violation of laws duly enacted by Congress. Specifically, he has\u2014\n**(i)**\nterminated Inspector Generals, the officers responsible for detecting and preventing waste by auditing and investigating their respective agencies\u2019 operations and personnel, in violation of the process stipulated by the Inspector Generals Act of 1974, as subsequently amended;\n**(ii)**\nterminated a member of the Merit Systems Protection Board, a tribunal created to address widespread public concerns about the Federal civil service; and\n**(iii)**\nunlawfully transmitted sensitive personal information of private citizens and government employees in violation of, among other Federal laws, the Privacy Act and the Administrative Procedure Act.\nIn all of this, Donald John Trump has willfully disregarded Federal laws and the Constitution, imperiled a coequal branch of Government, and threatened the integrity of the democratic system. He thereby betrayed his trust as President, abused the powers of the Presidency, acted in a manner grossly incompatible with self-governance and the rule of law, and has committed the High Crimes and Misdemeanors of obstruction of justice and effecting a wide-ranging scheme to destroy and corrupt the legal system and the powers of the courts under Article III of the Constitution.\nWherefore, Donald John Trump, by such conduct, has demonstrated that he is unfit to govern a Nation by and for the people, has acted in a manner grossly incompatible with self-governance and the rule of law, and will remain a threat to the Constitution if allowed to remain in office.\n#### Article II: Usurpation of the Appropriations Power\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that the President shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors . Further, Section 9 of Article I of the Constitution states that No money shall be drawn from the Treasury, but in Consequence of Appropriations made by Law . In his conduct of the office of President of the United States\u2014and in violation of his constitutional oath to faithfully to execute the office of President of the United States and, to the best of his ability, preserve, protect, and defend the Constitution of the United States, and in violation of his constitutional duty to take care that the laws be faithfully executed\u2014Donald John Trump has abused the powers of the Presidency in a manner offensive to, and subversive of, the Constitution, in that:\nUsing the powers of his high office, Donald John Trump unlawfully usurped Congress and its power to appropriate funds, thereby nullifying the Appropriations Clause in the Constitution and violating the Impoundment Control Act of 1974. Since taking office, he has signed numerous Executive Orders directing agencies to withhold funds appropriated by Congress. The President does not have the power to override spending laws or impound appropriated funds, a principle affirmed by numerous Supreme Court rulings.\nDonald John Trump has withheld funds and terminated en masse Federal employees and numerous Federal agencies and departments, including the following:\n**(1)**\nDirected the dismantling of the Department of Education. As enacted in the Department of Education Organization Act, signed into law by President Jimmy Carter, the Department of Education was established by Congress to create reform in the education system throughout the country, distribute Federal aid to students and places of learning, and prohibit discriminatory practices. The President does not have the authority to dismantle the Department of Education, and his signing of Executive Order 14242, which aims to Improving Education Outcomes by Empowering Parents, States, and Communities , violates the law and the Constitution.\n**(2)**\nUnlawfully directed the elimination of the United States Agency for International Development (USAID). As enacted in the Foreign Assistance Act of 1961, signed into law by President John F. Kennedy, USAID plays a crucial role in delivering foreign assistance worldwide, including disaster relief, conflict relief, combating global diseases, promoting educational programs, and enhancing food security in developing countries. By dismantling USAID and freezing foreign assistance, he has severed the United States from its humanitarian role as directed by Congress, leaving other countries and potentially our adversaries to fill in the role the United States has abandoned.\n**(3)**\nCreated the so-called Department of Government Efficiency (DOGE) , which has imposed payment holds and rescinded funds after disbursement. Donald John Trump has utilized DOGE to unlawfully block or impound appropriated funds to dozens of Federal agencies, including the National Institutes of Health, the Federal Aviation Administration, and the Department of Veterans Affairs. By impounding congressionally appropriated funds, Donald John Trump and DOGE have not only violated the law, but have negatively impacted the American people by cutting jobs, halting critical services, and rescinding grants for programs, in defiance of the express, constitutionally binding will of Congress.\nUsing the powers of his high office, Donald John Trump has unlawfully withheld congressionally appropriated funds and attempted to dismantle congressionally mandated agencies. By withholding funds and crippling agencies, he has prevented the Federal Government from performing critical duties here and abroad. He has threatened the well-being of United States citizens through the gross misconduct of his office, resulting in dire and life-threatening consequences on the world\u2019s most vulnerable populations.\nWherefore, Donald John Trump, by such conduct, has demonstrated that he is unfit to govern a Nation by and for the people, has acted in a manner grossly incompatible with self-governance and the rule of law, and will remain a threat to the Constitution if allowed to remain in office.\n#### Article III: Abuse of Trade Powers and International Aggression\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that the President shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors . Further, Section 8 of Article I of the Constitution states, Congress shall have Power To lay and collect Taxes, Duties, Imposts and Excises, . . . but all Duties, Imposts and Excises shall be uniform throughout the United States . In his conduct of the office of President of the United States\u2014and in violation of his constitutional oath to faithfully to execute the office of President of the United States and, to the best of his ability, preserve, protect, and defend the Constitution of the United States, and in violation of his constitutional duty to take care that the laws be faithfully executed\u2014Donald John Trump has abused the powers of the Presidency in a manner offensive to, and subversive of, the Constitution, in that:\nUsing the powers of his high office, Donald John Trump abused trade powers by imposing unjustifiable and unreasonable tariffs on foreign nations, causing a sharp decline in the United States economy and the economies of countries around the world, and declaring the false existence of a national security emergency to justify his actions. Donald John Trump\u2019s tariffs contradicted trade agreements established by his Administration and other administrations, including the duly ratified and binding treaty obligations of the United States, thereby breaking international laws and norms, leading to countries around the world to enact damaging tariffs on goods and services originating from the United States. His Liberation Day scheme, which imposed 10 percent tariffs on all countries, as well as additional tariffs based on a formula for reciprocity widely mocked as nonsensical, led to the most significant drop in the financial markets since the 2020 crash triggered by the COVID\u201319 pandemic.\nAdditionally, Donald John Trump has threatened foreign nations with invasion, the annexation of territory, and the occupation of sovereign territory through the use of military action. By doing this, he has implicated the United States and himself in violation of constitutionally binding treaty obligations, to include the North Atlantic Treaty of 1949, the General Treaty for Renunciation of War as an Instrument of National Policy of 1928, the Charter of the United Nations of 1945, and the Inter-American Treaty of Reciprocal Assistance of 1947. Donald John Trump threatened the following:\n**(1)**\nAnnexation of the sovereign country of Canada. Donald John Trump has negatively impacted the deep and historic relationship between the United States and Canada by stating numerous times that Canada should become the 51st State, under the threat of both economic coercion and military force.\n**(2)**\nUnlawful and aggressive military action within Mexico, to include drone strikes and the use of special operations military personnel, ostensibly against drug cartels, in violation of the sovereignty and territorial integrity of that country and without any congressional authorization to use military force.\n**(3)**\nAnnexation of Greenland, an autonomous territory in the Kingdom of Denmark. Donald John Trump has continued to use hostile language aimed at taking control of Greenland, stating that the United States will go as far as we have to go to obtain control of Greenland. He has refused to rule out military action to gain control of the territory, in violation of international law and despite Denmark\u2019s longstanding alliance and friendly relations with the United States.\n**(4)**\nAnnexation of the Panama Canal, owned and controlled by Panama. During a joint session speech to Congress, Donald John Trump stated that his Administration will be reclaiming the Panama Canal . He has refused to rule out military or economic action against the sovereign country.\n**(5)**\nAnnexation of the Gaza Strip, involving the forced resettlement of the Palestinian population to the surrounding countries. Donald John Trump has stated that the United States will take over the Gaza Strip and own it . His proposal of taking over the Gaza Strip and the expulsion of its population violates international law, including the Convention on the Prevention and Punishment of the Crime of Genocide, would be unconstitutional absent the approval of the United States Congress, and is profoundly unserious in light of the grave humanitarian situation and ongoing armed conflict in Gaza.\nUsing the powers of his high office, Donald John Trump has unlawfully conducted himself, bringing shame and embarrassment to the office of the Presidency and the people of the United States. He has betrayed the trust of the Nation to conduct meaningful diplomatic negotiations as its chief diplomat and failed to maintain peaceful economic and defense relations with foreign countries. He has threatened the security of the United States through gross misconduct of his office, prompting hostilities towards Americans here and abroad, as well as foreign nations warning their citizens against visiting the United States, further harming the Nation\u2019s economy.\nWherefore, Donald John Trump, by such conduct, has demonstrated that he is unfit to govern a Nation by and for the people, has acted in a manner grossly incompatible with self-governance and the rule of law, and will remain a threat to the Constitution if allowed to remain in office.\n#### Article IV: Violation of First Amendment Rights\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that the President shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors . Further, the First Amendment of the Constitution states Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances . In his conduct of the office of President of the United States\u2014and in violation of his constitutional oath to faithfully to execute the office of President of the United States and, to the best of his ability, preserve, protect, and defend the Constitution of the United States, and in violation of his constitutional duty to take care that the laws be faithfully executed\u2014Donald John Trump has abused the powers of the Presidency in a manner offensive to, and subversive of, the Constitution, in that:\nBy his orders and directions to subordinates, retaliated against law firms and attorneys who have advised or represented, or been associated with those who advise or represent, litigants who displease him, in violation of the Constitution\u2019s prohibition on retaliation against individuals for engaging in First Amendment-protected conduct, including the right to petition the government for redress of grievances. Specifically, he has, barred attorneys at certain law firms from access to Federal buildings, arbitrarily revoked security clearances without a reasonable basis, threatened to cancel Federal contracts with any entity engaging the targeted attorneys and firms, and demanded pro bono services from law firms in exchange for the discontinuation of the punitive Executive orders.\nAdditionally, Donald John Trump has engaged in a pattern of unconstitutional, unlawful, and corrupt retaliation against critics and political opponents, a flagrant violation of constitutional rights protected by the First Amendment. He has weaponized the Department of Justice and other agencies to engage in spurious investigations and harassment, with no basis in law, of public figures and his perceived political enemies.\nSince taking office, Donald John Trump has directed the Department of Justice to dismiss more than a dozen prosecutors who were involved in investigations against him after he left office in 2021. The Department of Justice has subsequently launched investigations into officials involved in prior probes against Donald John Trump, in some cases against individuals specifically named and accused in flagrantly improper Executive orders.\nFurthermore, he has made direct and unambiguous public statements threatening media outlets, current and former officeholders, and advocacy organizations. He has pursued meritless litigation, leveraged his public office for private gain, and perverted the course of justice and the integrity of the judicial system to extract tens of millions of dollars in putative settlements, effectively acting as a conduit for flagrant bribery and extortion. He has restricted the access of the Associated Press after they refused to use the name Gulf of America in their reporting and has defied court orders to cease this unconstitutional action. He has also threatened current and former members of Congress for the exercise of their legislative and oversight functions, an attack on the independence of Congress as a coequal branch of government as established by the Constitution's Article I Vesting Clause, and by the Constitution\u2019s Speech or Debate Clause, in addition to the First Amendment.\nFor example, Donald John Trump has repeatedly threatened members of the House Select Committee on the January 6th Attack on the United States Capitol, which investigated the attack on the Capitol that Donald John Trump instigated. Donald John Trump has sought to intimidate the members and staff of the United States House Select Committee on the January 6th Attack, stating that they should fully understand that they are subject to investigation at the highest level and expressing a desire to remove the pardons they received, stating The Pardons that Sleepy Joe Biden gave to the Unselect Committee of Political Thugs, and many others, are hereby declared [void, vacant, and of no further force or effect] .\nDonald John Trump has made it clear that he will not rest until all of his perceived political enemies are eliminated. In a speech addressing his Department of Justice subordinates, Donald John Trump further laid out his fascist vision for the Department of Justice. He has targeted watchdog organizations like the Citizens for Responsibility and Ethics in Washington, calling them scum and independent media outlets like CNN and MSNBC, labelling them as organizations that literally write 97.6 percent bad about me, are political arms of the Democrat Party. And in my opinion, they are really corrupt and they are illegal. What they do is illegal. . He has stated that newspapers critical of him are really no different than a highly paid political operative. And it has to stop. It has to be illegal. It\u2019s influencing judges . . . it just cannot be legal. .\nBy these and many other actions, he has sought to outlaw dissent, opposition, and criticism of himself and his Administration. This attack on the constitutional rights to freedom of speech, and of association, and of the right to petition the government for redress of grievances, is wholly incompatible with the rights and liberties of the People of the United States as a self-governing people under the rule of law.\nIn purpose and effect, he has attempted to suppress dissent and opposition, casting a chilling effect over the public discourse, and striking at the core freedoms essential to a free society and democratic elections under the Constitution.\nWherefore, Donald John Trump, by such conduct, has demonstrated that he is unfit to govern a Nation by and for the people, has acted in a manner grossly incompatible with self-governance and the rule of law, and will remain a threat to the Constitution if allowed to remain in office.\n#### Article V: Creation of Unlawful Office\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that the President shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors . Further, Section 2 of Article II of the Constitution states that the President shall appoint Ambassadors, other public Ministers and Consuls, Judges of the supreme Court, and all other Officers of the United States \u2026 but the Congress may by Law vest the Appointment of such inferior Officers, as they think proper, in the President alone, in the Courts of Law, or in the Heads of Departments . In his conduct of the office of President of the United States\u2014and in violation of his constitutional oath to faithfully to execute the office of President of the United States and, to the best of his ability, preserve, protect, and defend the Constitution of the United States, and in violation of his constitutional duty to take care that the laws be faithfully executed\u2014Donald John Trump has abused the powers of the Presidency in a manner offensive to, and subversive of, the Constitution, in that:\nUsing the powers of his high office, Donald John Trump has, through unlawful orders and directives, created an unlawful office, the so-called Department of Government Efficiency ( DOGE ), and assigned an extensive range of unlawful powers, effectively granting this flagrantly unconstitutional creation significant control over the executive branch. Donald John Trump has appointed Mr. Elon Musk as the de facto head of this contrived entity, which was not created or funded by any law, without a formal title or office. These actions have been in direct violation of the Constitution\u2019s requirement that principal officers of the United States must be created by law and their appointees confirmed by the Senate, and that inferior offices must be created by law with their appointment vested as Congress may determine.\nAdditionally, he has vested these powers in Mr. Musk without complying with the constitutional requirement that all officers of the United States be commissioned by the President and swear an oath of office to support the Constitution. Mr. Musk has been designated as a special government employee of the White House Office, in violation of statutory authorization and restrictions on such designations. This false claim has also been used to commit violations of the ethics, disclosure, and conflict-of-interest laws applicable to government officers and regular employees.\nContrary to the Government\u2019s claims in court, Mr. Musk has exercised de facto control over DOGE and, through it, control over a wide range of Government departments and agencies. This unmistakable reality has been repeatedly and openly stated by the Trump Administration, including by Donald John Trump\u2019s own address to Congress on March 4, 2025. In this capacity, Mr. Musk and his subordinates have undertaken numerous violations of the Constitution and laws, including by\u2014\n**(1)**\nimpoundment of funds appropriated by Congress;\n**(2)**\nviolations of privacy and security laws with respect to sensitive information systems, personally identifiable information, and classified material; and\n**(3)**\ntermination of government employees under false pretenses and in violation of civil service laws.\nThese actions have vastly exceeded the terms of the formal executive orders purporting to create DOGE under the direction of a U.S. DOGE Service Administrator , an office which remained vacant for several weeks, with the Government\u2019s own attorneys claiming in court that the official head of DOGE was unknown to them. Since that time, a nominal Administrator has been named, despite the repeated avowals from the President and his Administration that Mr. Musk controls and directs DOGE, as confirmed by ample public reporting and Mr. Musk\u2019s own statements.\nDonald John Trump has abused the powers of his high office and breached the public trust by establishing the so-called Department of Government Efficiency and unconstitutionally placing Mr. Musk in control of this entity, knowingly provided false testimony to the court regarding the leadership of the said entity, and directing the unlawful entity to implement his agenda, in violation of the Constitution\u2019s objective of establishing Justice and fundamental rules for how the executive branch of the United States is to be structured and how persons may be appointed to public office.\nWherefore, Donald John Trump, by such conduct, has demonstrated that he is unfit to govern a Nation by and for the people, has acted in a manner grossly incompatible with self-governance and the rule of law, and will remain a threat to the Constitution if allowed to remain in office.\n#### Article VI: Bribery and Corruption\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that the President shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors . Further, Section 9 of Article I of the Constitution states that no Person holding any Office of Profit or Trust under them, shall, without the Consent of the Congress, accept of any present, Emolument, Office, or Title, of any kind whatever, from any \u2026 foreign State . In his conduct of the office of President of the United States\u2014and in violation of his constitutional oath to faithfully to execute the office of President of the United States and, to the best of his ability, preserve, protect, and defend the Constitution of the United States, and in violation of his constitutional duty to take care that the laws be faithfully executed\u2014Donald John Trump has abused the powers of the Presidency in a manner offensive to, and subversive of, the Constitution, in that:\nDonald John Trump has engaged in a pattern of unlawful corruption for the personal profit of himself and his associates, soliciting and accepting bribes in exchange for official actions, policy influence, and favorable treatment from the Administration. In so doing, he has, beyond a reasonable doubt, profiteered from public office on a scale unprecedented in American history.\nDonald John Trump has engaged in fraudulent con artist schemes through pump and dump or rug pull tactics for cryptocurrency tokens he has created, and at the same time, enabled a direct conduit for bribes paid to him in exchange for official actions.\nDonald John Trump has also leveraged the threat of hostile government action and the corresponding offer of preferential treatment in order to extract large payments in the form of settlements for meritless and vexatious litigation he pursues in his personal capacity, thereby corrupting both the executive branch and the judiciary. To advance this end, Donald John Trump solicited and received $940,000,000 in pro bono services from prominent law firms to help causes he personally supports.\nDonald John Trump has refused to divest himself or take any steps to prevent conflicts of interest in his substantial personal business ventures, creating another conduit for the payment of bribes.\nDonald John Trump has permitted and encouraged his subordinates to violate laws regarding ethics, disclosures, and self-dealing, and through these actions, he has enabled and encouraged corruption and graft by his relatives, associates, and political allies.\nDonald John Trump has, in these ways and others, solicited payments from foreign governments for corrupt purposes and in flagrant violation of the Constitution\u2019s prohibition on foreign emoluments.\nWherefore, Donald John Trump, by such conduct, has demonstrated that he is unfit to govern a Nation by and for the people, has acted in a manner grossly incompatible with self-governance and the rule of law, and will remain a threat to the Constitution if allowed to remain in office.\n#### Article VII: Tyranny\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that the President shall be removed from Office on Impeachment for, and Conviction of, Treason, Bribery, or other high Crimes and Misdemeanors . Further, the system of checks and balances, as well as the separation of powers, as defined in the Constitution, work to ensure that the Office of the President does not become tyrannical. In his conduct of the office of President of the United States\u2014and in violation of his constitutional oath to faithfully to execute the office of President of the United States and, to the best of his ability, preserve, protect, and defend the Constitution of the United States, and in violation of his constitutional duty to take care that the laws be faithfully executed\u2014Donald John Trump has abused the powers of the Presidency in a manner offensive to, and subversive of, the Constitution, in that:\nHe has, by his actions and statements, sought to establish himself as tyrant, dictator, and autocrat over the People of the United States, usurping unto himself the constitutional powers of Congress, the courts, and the States, and powers illegitimate and beyond the scope of lawful government altogether.\nHe has claimed for himself absolute and arbitrary power, the ability to suspend laws at whim, and utterly disregarded and betrayed his oath to faithfully execute the office of President of the United States and to preserve, protect, and defend the Constitution of the United States.\nHe has denied and violated the right of the People of the United States to freedom of speech, and of assembly, and to petition the government for redress of grievances.\nHe has denied and violated the right of the People of the United States to due process of law and equal protection under the laws, to fair and impartial independent courts, and to legal counsel.\nHe has sought to intimidate and coerce, by means including the threat of unlawful prosecutions and by encouraging violence and threats of violence, the Representatives and Senators in Congress.\nHe has denied and violated the separation of powers and the Constitution\u2019s system of checks and balances, arrogating unto himself the legislative and judicial powers, including the power of Congress to levy taxes, appropriate public funds, direct the organization of officers and agencies of the executive branch, and to make laws.\nHe has sought to intimidate, coerce, and extort the officers of the several States, including those elected by the People thereof, and thereby sought to commandeer the several States, in violation of their sovereignty and the system of federalism established by the Constitution of the United States.\nHe has sought to abrogate the citizenship clause of the 14th Amendment to the Constitution, by means including the issuance of an executive order that directs executive departments and agencies to withhold citizenship from certain classes of persons who are born within the United States.\nHe has repeatedly threatened and suggested that he intends to violate the Presidential term limits established by the 22d Amendment to the Constitution, and adopted overtly monarchical aspirations and affectations, including by invoking and endorsing theories that he is above the law or that his personal will constitutes the law.\nIn all of this, Donald John Trump has willfully disregarded Federal laws and the Constitution, imperiled a coequal branch of Government, and threatened the integrity of the democratic system. He thereby betrayed his trust as President, abused the powers of the Presidency, acted in a manner grossly incompatible with self-governance and the rule of law, and has committed High Crimes and Misdemeanors in attempting to establish himself as a lawless tyrant to the manifest injury of the people of the United States.\nWherefore, Donald John Trump, by such conduct, has demonstrated that he is unfit to govern a Nation by and for the people, has acted in a manner grossly incompatible with self-governance and the rule of law, and will remain a threat to the Constitution if allowed to remain in office.",
      "versionDate": "2025-04-28",
      "versionType": "IH"
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
            "updateDate": "2025-05-16T15:51:43Z"
          },
          {
            "name": "Alliances",
            "updateDate": "2025-05-16T15:49:09Z"
          },
          {
            "name": "Appropriations",
            "updateDate": "2025-05-16T15:47:40Z"
          },
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-05-16T15:45:56Z"
          },
          {
            "name": "Canada",
            "updateDate": "2025-05-16T15:49:28Z"
          },
          {
            "name": "Citizenship and naturalization",
            "updateDate": "2025-05-16T15:52:07Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-05-16T15:43:56Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-05-16T15:44:08Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-05-16T15:45:14Z"
          },
          {
            "name": "Currency",
            "updateDate": "2025-05-16T15:51:50Z"
          },
          {
            "name": "Denmark",
            "updateDate": "2025-05-16T15:49:48Z"
          },
          {
            "name": "Department of Education",
            "updateDate": "2025-05-16T15:47:47Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2025-05-16T15:44:47Z"
          },
          {
            "name": "Department of Transportation",
            "updateDate": "2025-05-16T15:48:16Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-05-16T15:48:08Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-05-16T15:46:41Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-05-16T15:50:19Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-05-16T15:46:24Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-05-16T15:48:39Z"
          },
          {
            "name": "El Salvador",
            "updateDate": "2025-05-16T15:46:02Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-05-16T15:46:47Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-05-16T15:49:53Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-05-16T15:50:51Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-05-16T15:45:33Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-05-16T15:51:08Z"
          },
          {
            "name": "First Amendment rights",
            "updateDate": "2025-05-16T15:44:21Z"
          },
          {
            "name": "Gaza Strip",
            "updateDate": "2025-05-16T15:50:05Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-05-16T15:45:04Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-05-16T15:44:27Z"
          },
          {
            "name": "Greenland",
            "updateDate": "2025-05-16T15:49:43Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-05-16T15:48:23Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-05-16T15:45:45Z"
          },
          {
            "name": "International law and treaties",
            "updateDate": "2025-05-16T15:49:16Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-05-16T15:45:22Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2025-05-16T15:46:09Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-05-16T15:44:55Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-05-16T15:50:29Z"
          },
          {
            "name": "Merit Systems Protection Board",
            "updateDate": "2025-05-16T15:46:29Z"
          },
          {
            "name": "Mexico",
            "updateDate": "2025-05-16T15:49:32Z"
          },
          {
            "name": "National Institutes of Health (NIH)",
            "updateDate": "2025-05-16T15:48:01Z"
          },
          {
            "name": "News media and reporting",
            "updateDate": "2025-05-16T15:50:34Z"
          },
          {
            "name": "North America",
            "updateDate": "2025-05-16T15:49:38Z"
          },
          {
            "name": "Palestinians",
            "updateDate": "2025-05-16T15:50:11Z"
          },
          {
            "name": "Panama Canal",
            "updateDate": "2025-05-16T15:49:58Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-05-16T15:43:49Z"
          },
          {
            "name": "Protest and dissent",
            "updateDate": "2025-05-16T15:50:43Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-05-16T15:46:35Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2025-05-16T15:50:23Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-05-16T15:49:22Z"
          },
          {
            "name": "Subversive activities",
            "updateDate": "2025-05-16T15:51:59Z"
          },
          {
            "name": "Supreme Court",
            "updateDate": "2025-05-16T15:46:17Z"
          },
          {
            "name": "Tariffs",
            "updateDate": "2025-05-16T15:49:02Z"
          },
          {
            "name": "Transportation programs funding",
            "updateDate": "2025-05-16T15:48:30Z"
          },
          {
            "name": "U.S. Agency for International Development (USAID)",
            "updateDate": "2025-05-16T15:47:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-12T10:33:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-28",
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
          "measure-id": "id119hres353",
          "measure-number": "353",
          "measure-type": "hres",
          "orig-publish-date": "2025-04-28",
          "originChamber": "HOUSE",
          "update-date": "2025-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres353v00",
            "update-date": "2025-05-12"
          },
          "action-date": "2025-04-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution impeaches President Donald Trump for high crimes and misdemeanors.</p><p>The resolution sets forth seven articles of impeachment of the President: (1) obstruction of justice, violation of due process, and a breach of the duty to faithfully execute laws; (2) usurpation of Congress' appropriations power; (3) abuse of trade powers and international aggression; (4) violation of First Amendment rights; (5) creation of an unlawful office; (6) bribery and corruption; and (7) tyranny.</p>"
        },
        "title": "Impeaching Donald John Trump, President of the United States, for high crimes and misdemeanors."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres353.xml",
    "summary": {
      "actionDate": "2025-04-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution impeaches President Donald Trump for high crimes and misdemeanors.</p><p>The resolution sets forth seven articles of impeachment of the President: (1) obstruction of justice, violation of due process, and a breach of the duty to faithfully execute laws; (2) usurpation of Congress' appropriations power; (3) abuse of trade powers and international aggression; (4) violation of First Amendment rights; (5) creation of an unlawful office; (6) bribery and corruption; and (7) tyranny.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119hres353"
    },
    "title": "Impeaching Donald John Trump, President of the United States, for high crimes and misdemeanors."
  },
  "summaries": [
    {
      "actionDate": "2025-04-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution impeaches President Donald Trump for high crimes and misdemeanors.</p><p>The resolution sets forth seven articles of impeachment of the President: (1) obstruction of justice, violation of due process, and a breach of the duty to faithfully execute laws; (2) usurpation of Congress' appropriations power; (3) abuse of trade powers and international aggression; (4) violation of First Amendment rights; (5) creation of an unlawful office; (6) bribery and corruption; and (7) tyranny.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119hres353"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres353ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Impeaching Donald John Trump, President of the United States, for high crimes and misdemeanors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T09:18:17Z"
    },
    {
      "title": "Impeaching Donald John Trump, President of the United States, for high crimes and misdemeanors.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T08:05:49Z"
    }
  ]
}
```
